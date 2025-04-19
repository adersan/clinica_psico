from django.urls import path
from .views import ConsultaListCreateView, ConsultaRetrieveUpdateDestroyView

urlpatterns = [
    path('consultas/', ConsultaListCreateView.as_view(), name='consulta-list-create'),
    path('consultas/<int:pk>/', ConsultaRetrieveUpdateDestroyView.as_view(), name='consulta-detail'),
]
