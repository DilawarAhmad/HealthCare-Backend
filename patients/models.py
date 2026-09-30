from django.db import models
from users.models import User

class Patient(models.Model):
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=255
    )
    age = models.IntegerField()
    gender = models.CharField(
        max_length=20
    )
    disease = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )