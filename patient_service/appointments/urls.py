from django.urls import path
from . import views
from .views import ConsultaListCreateView, ConsultaRetrieveUpdateDestroyView, dashboard_agendamentos


urlpatterns = [
    path('consultas/', ConsultaListCreateView.as_view(), name='consulta-list-create'),
    path('consultas/<int:pk>/', ConsultaRetrieveUpdateDestroyView.as_view(), name='consulta-detail'),
    path('dashboard/agendamentos/', views.dashboard_agendamentos, name='dashboard_agendamentos'),
    
    # Nova rota visual
    path('dashboard-agendamentos/', dashboard_agendamentos, name='dashboard-agendamentos'),
]
