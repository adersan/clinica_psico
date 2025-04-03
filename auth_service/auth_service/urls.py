from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

#Criar uma view simples para a página inicial
def home(request):
    return JsonResponse({"message": "Bem-vindo ao Auth Service da Clínica PSICO+"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),  # Confirme que está correto
    path('', home),  #Define a rota para "/"
]
