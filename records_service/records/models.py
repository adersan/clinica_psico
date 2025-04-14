# records/models.py

from django.db import models

class Record(models.Model):
    paciente_id = models.IntegerField()
    data = models.DateField(auto_now_add=True)
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.titulo} - Paciente #{self.paciente_id}"
