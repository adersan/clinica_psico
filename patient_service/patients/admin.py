from django.contrib import admin
from .models import Paciente, Endereco

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'email', 'telefone')  # Campos que aparecem na listagem
    search_fields = ('nome', 'cpf', 'email')             # Campos pesquisáveis
    list_filter = ('data_nascimento',)                   # Filtros laterais
    ordering = ('nome',)                                 # Ordenação padrão por nome

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('rua', 'numero', 'bairro', 'cidade', 'estado', 'cep')
    search_fields = ('rua', 'bairro', 'cidade', 'cep')
    ordering = ('cidade',)
