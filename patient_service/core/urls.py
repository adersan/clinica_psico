from django.contrib import admin
from django.urls import path, include, include
from django.conf import settings
from django.http import JsonResponse

def home(request):
    return JsonResponse({"mensagem": "Serviço de pacientes ativo."})

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include('patients.urls')),
    
]
