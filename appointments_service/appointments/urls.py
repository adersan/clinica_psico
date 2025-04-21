from django.urls import path
from .views import (
    ConsultaListCreateView,
    ConsultaRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('', ConsultaListCreateView.as_view(), name='consulta-list-create'),
    path('<int:pk>/', ConsultaRetrieveUpdateDestroyView.as_view(), name='consulta-detail'),
]
