from django.urls import path
from .views import (
    MappingListCreateView,
    PatientMappingsView,
    MappingDeleteView
)

urlpatterns = [
    path(
        "",
        MappingListCreateView.as_view(),
        name="mapping-list-create"
    ),
    path(
        "<int:patient_id>/",
        PatientMappingsView.as_view(),
        name="patient-mappings"
    ),
    path(
        "delete/<int:id>/",
        MappingDeleteView.as_view(),
        name="mapping-delete"
    ),
]