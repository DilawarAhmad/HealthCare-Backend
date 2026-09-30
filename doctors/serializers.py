from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"

    def validate_experience(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Experience cannot be negative."
            )
        return value