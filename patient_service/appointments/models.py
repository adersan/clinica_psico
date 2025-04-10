
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from patients.models import Paciente  # ajuste conforme sua estrutura de microserviço

class StatusConsulta(models.TextChoices):
    AGENDADA = 'agendada', 'Agendada'
    CONFIRMADA = 'confirmada', 'Confirmada'
    CANCELADA = 'cancelada', 'Cancelada'
    REALIZADA = 'realizada', 'Realizada'

class TipoConsulta(models.TextChoices):
    INDIVIDUAL = 'individual', 'Individual'
    GRUPO = 'grupo', 'Grupo'
    AVALIACAO = 'avaliacao', 'Avaliação'
    RETORNO = 'retorno', 'Retorno'

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='consultas')
    profissional = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='consultas')
    data = models.DateField()
    hora = models.TimeField(default="12:00")
    status = models.CharField(max_length=20, choices=StatusConsulta.choices, default=StatusConsulta.AGENDADA)
    tipo_consulta = models.CharField(max_length=20, choices=TipoConsulta.choices, default=TipoConsulta.INDIVIDUAL)
    participantes = models.TextField(blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(default=timezone.now)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('profissional', 'data', 'hora')

    def __str__(self):
        return f"{self.paciente.nome} - {self.data} {self.hora} ({self.status})"
