from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import PatientDoctorMapping
from .serializers import (
    PatientDoctorMappingSerializer
)

#List and Create view for Mappings
class MappingListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    # Get all the mappings 
    def get(self, request):
        mappings = (PatientDoctorMapping.objects.all())

        serializer = (
            PatientDoctorMappingSerializer(
                mappings,
                many=True
            )
        )

        return Response(
            serializer.data
        )

    # Create new mapping of Patient and Doctor
    def post(self, request):
        serializer = (
            PatientDoctorMappingSerializer(
                data=request.data
            )
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

# Details View for Mappings 
class PatientMappingsView(
    APIView
):
    permission_classes = [
        IsAuthenticated
    ]

    # Get Doctors assigned to Patient
    def get(self, request, patient_id):
        mappings = (
            PatientDoctorMapping.objects
            .filter(
                patient_id=patient_id
            )
        )
        serializer = (
            PatientDoctorMappingSerializer(
                mappings,
                many=True
            )
        )
        return Response(
            serializer.data
        )


class MappingDeleteView(
    APIView
):
    permission_classes = [
        IsAuthenticated
    ]
    # Delete the mappings of Patient using his id
    def delete(self, request, id):
        try:
            mapping = (
                PatientDoctorMapping.objects
                .get(id=id)
            )
        except (
            PatientDoctorMapping
            .DoesNotExist
        ):
            return Response(
                {
                    "error":
                    "Mapping not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        mapping.delete()
        return Response(
            {
                "message":
                "Doctor removed from patient"
            },
            status=status.HTTP_200_OK
        )