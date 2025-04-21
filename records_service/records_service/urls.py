from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home(request):
    return JsonResponse({"mensagem": "Serviço de records ativo."})

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include('records.urls')),  # ← nossa API
]
