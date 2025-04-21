# professionals/urls.py
from django.urls import path
from .views import (
    ProfissionalListCreateView,
    ProfissionalRetrieveUpdateDestroyView
)

urlpatterns = [
    path('profissionais/', ProfissionalListCreateView.as_view(), name='profissional-list-create'),
    path('profissionais/<int:pk>/', ProfissionalRetrieveUpdateDestroyView.as_view(), name='profissional-detail'),
]
