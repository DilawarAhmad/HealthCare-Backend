from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Patient
from .serializers import PatientSerializer

# Create and List Patients View
class PatientListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    # Get all the Patients Created by the Requesting User
    def get(self, request):
        patients = Patient.objects.filter(
            created_by=request.user
        )
        serializer = PatientSerializer(
            patients,
            many=True
        )
        return Response(serializer.data)

    # Create New Patient
    def post(self, request):
        serializer = PatientSerializer(
            data=request.data
        )
        if serializer.is_valid():
            serializer.save(
                created_by=request.user
            )
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

# Detail View about the Patients
class PatientDetailView(APIView):
    permission_classes = [IsAuthenticated]

    # Get Patient details using his id helper function
    def get_object(self, id, user):
        try:
            return Patient.objects.get(
                id=id,
                created_by=user
            )
        except Patient.DoesNotExist:
            return None

    # Get Patient Details from his id and requesting user 
    def get(self, request, id):
        patient = self.get_object(
            id,
            request.user
        )
        if not patient:
            return Response(
                {"error": "Patient not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = PatientSerializer(
            patient
        )
        return Response(serializer.data)

    # Update the Patient using his id
    def put(self, request, id):
        patient = self.get_object(
            id,
            request.user
        )
        if not patient:
            return Response(
                {"error": "Patient not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = PatientSerializer(
            patient,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    # Delete Patient using his id
    def delete(self, request, id):
        patient = self.get_object(
            id,
            request.user
        )
        if not patient:
            return Response(
                {"error": "Patient not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        patient.delete()
        return Response(
            {"message": "Patient deleted successfully"},
            status=status.HTTP_200_OK
        )