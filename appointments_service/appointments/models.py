from django.db import models

class Consulta(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
        ('concluida', 'Concluída'),
    ]

    CONVENIO_CHOICES = [
        ('', 'Selecione'),
        ('Particular', 'Particular'),
        ('Plano de Saude', 'Plano de Saúde'),
        ('SUS', 'SUS'),
        ('Popular', 'Popular'),
        ('Parcerias', 'Parcerias'),
        ('Filantrópico', 'Filantrópico'),
        ('Domiciliar', 'Domiciliar'),
        ('Online/Telemedicina', 'Online/Telemedicina'),
    ]

    paciente_id = models.IntegerField()  # apenas o ID vindo do patients_service
    profissional_id = models.IntegerField()  # apenas o ID vindo do professionals_service

    data = models.DateField()
    hora = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    observacoes = models.TextField(blank=True)

    tipo_convenio = models.CharField(max_length=50, choices=CONVENIO_CHOICES, default='', blank=True)
    nome_convenio = models.CharField(max_length=100, blank=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Consulta ID {self.id} - Paciente {self.paciente_id} / Profissional {self.profissional_id}"
