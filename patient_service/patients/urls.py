
from django.urls import path
from .views import PacienteListCreateView, PacienteRetrieveUpdateDestroyView

urlpatterns = [
    path('pacientes/', PacienteListCreateView.as_view(), name='paciente-list-create'),
    path('pacientes/<int:pk>/', PacienteRetrieveUpdateDestroyView.as_view(), name='paciente-detail'),
]
