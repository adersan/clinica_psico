from django.urls import path
from .views import PatientListCreateView, PatientRetrieveUpdateDestroyView

urlpatterns = [
    path('pacientes/', PatientListCreateView.as_view(), name='patient-list-create'),
    path('pacientes/<int:pk>/', PatientRetrieveUpdateDestroyView.as_view(), name='patient-detail'),
]
