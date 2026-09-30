from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Doctor
from .serializers import DoctorSerializer

# Create and List Doctors View
class DoctorListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    # Get all Doctors
    def get(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(
            doctors,
            many=True
        )
        return Response(serializer.data)

    #Create new Doctor
    def post(self, request):
        serializer = DoctorSerializer(
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class DoctorDetailView(APIView):
    permission_classes = [IsAuthenticated]

    # Get Doctor Details by ID Helper function
    def get_object(self, id):
        try:
            return Doctor.objects.get(id=id)
        except Doctor.DoesNotExist:
            return None

    # Get Doctor Details by ID using helper function
    def get(self, request, id):
        doctor = self.get_object(id)
        if not doctor:
            return Response(
                {"error": "Doctor not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = DoctorSerializer(
            doctor
        )
        return Response(serializer.data)

    # Update Doctor Details using ID
    def put(self, request, id):
        doctor = self.get_object(id)
        if not doctor:
            return Response(
                {"error": "Doctor not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = DoctorSerializer(
            doctor,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    # Delete Doctor using his ID
    def delete(self, request, id):
        doctor = self.get_object(id)
        if not doctor:
            return Response(
                {"error": "Doctor not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        doctor.delete()
        return Response(
            {"message": "Doctor deleted successfully"},
            status=status.HTTP_200_OK
        )