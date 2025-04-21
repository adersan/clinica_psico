from django.contrib import admin
from .models import Consulta

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ['id', 'paciente_id', 'profissional_id', 'data', 'hora', 'status']
    list_filter = ['status', 'data']
    search_fields = ['paciente_id', 'profissional_id', 'nome_convenio']
