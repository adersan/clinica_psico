# notifications/models.py
from django.db import models
from django.utils import timezone



class Notificacao(models.Model):
    TIPOS = [
        ('email', 'E-mail'),
        ('sms', 'SMS'),
        ('whatsapp', 'WhatsApp')
    ]

    destino = models.CharField(max_length=255)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    assunto = models.CharField(max_length=255, blank=True)
    mensagem = models.TextField()
    enviada = models.BooleanField(default=False)
    criada_em = models.DateTimeField(auto_now_add=True)
    atualizada_em = models.DateTimeField(auto_now=True)
    agendada_em = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.tipo} para {self.destino}"
    
    class Meta:
        verbose_name = "Notificação"
        verbose_name_plural = "Notificações"
