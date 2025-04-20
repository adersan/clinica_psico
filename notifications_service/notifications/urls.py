from django.urls import path
from .views import (
    NotificacaoListCreateView,
    NotificacaoRetrieveUpdateDestroyView,
    EnviarWhatsappView
)

urlpatterns = [
    path('', NotificacaoListCreateView.as_view(), name='notificacao-list-create'),
    path('<int:pk>/', NotificacaoRetrieveUpdateDestroyView.as_view(), name='notificacao-detail'),
    path('whatsapp/', EnviarWhatsappView.as_view(), name='notificacao-whatsapp'),
]
