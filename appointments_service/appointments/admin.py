from django.contrib import admin
from .models import Consulta

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'profissional', 'data', 'hora', 'status')
    search_fields = ('paciente', 'profissional')
    list_filter = ('status', 'data')
