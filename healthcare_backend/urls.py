from django.urls import path
from django.urls import include

urlpatterns = [

    path(
        "api/auth/",
        include("users.urls")
    ),

    path(
        "api/patients/",
        include("patients.urls")
    ),

    path(
        "api/doctors/",
        include("doctors.urls")
    ),

    path(
        "api/mappings/",
        include("mappings.urls")
    ),
]