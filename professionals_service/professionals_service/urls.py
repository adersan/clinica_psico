from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home(request):
    return JsonResponse({"mensagem": "Serviço de profissionais ativo."})

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include('professionals.urls')),  # <- Certifique-se disso
]
