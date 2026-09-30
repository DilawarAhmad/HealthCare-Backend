from django.db import models


class Doctor(models.Model):
    name = models.CharField(
        max_length=255
    )
    specialization = models.CharField(
        max_length=255
    )
    experience = models.IntegerField()
    hospital = models.CharField(
        max_length=255
    )