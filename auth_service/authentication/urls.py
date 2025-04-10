from django.urls import path
from .views import (
    RegisterView, LoginView, LogoutView,
    login_view, home_view, dashboard_view,
    register_view, dashboard_agendamentos,
    dashboard_pacientes
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # API
    path('cadastro/', register_view, name='register-page'),      # Formulário de cadastro visual
    path('api/login/', LoginView.as_view(), name='api-login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('dashboard/agendamentos/', dashboard_agendamentos, name='dashboard_agendamentos'),
    path('dashboard/pacientes/', dashboard_pacientes, name='dashboard_pacientes'),
   
]
