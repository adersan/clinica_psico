from django.urls import path
from .views import (ProfissionalListCreateView, ProfissionalRetrieveUpdateDestroyView,)

urlpatterns = [
    path('profissionais/', ProfissionalListCreateView.as_view(), name='profissionais-list-create'),
    path('profissionais/<int:pk>/', ProfissionalRetrieveUpdateDestroyView.as_view(), name='profissionais-detail'),
]
