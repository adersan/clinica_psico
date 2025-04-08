from django.db import models
from django.contrib.auth.models import User
from patients.models import Paciente  # ajuste o import conforme a organização dos microserviços

class StatusConsulta(models.TextChoices):
    AGENDADA = 'agendada', 'Agendada'
    CONFIRMADA = 'confirmada', 'Confirmada'
    CANCELADA = 'cancelada', 'Cancelada'
    REALIZADA = 'realizada', 'Realizada'

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='consultas')
    profissional = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='consultas')
    data = models.DateField()
    hora = models.TimeField()
    observacoes = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=StatusConsulta.choices,
        default=StatusConsulta.AGENDADA
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.paciente.nome} - {self.data} {self.hora} ({self.status})"
