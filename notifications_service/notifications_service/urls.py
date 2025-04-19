from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home(request):
    return JsonResponse({"mensagem": "Serviço de notificações ativo."})

urlpatterns = [
    path('', home),  # ← adiciona uma resposta simples na raiz
    path('admin/', admin.site.urls),
    path('api/notificacoes/', include('notifications.urls')),
]
