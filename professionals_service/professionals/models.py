from django.db import models
from django.utils import timezone

class Profissional(models.Model):
    CONSELHOS_CHOICES = [
        ('', 'Selecione'),
        ('CRM', 'CRM'),
        ('COREN', 'COREN'),
        ('CRP', 'CRP'),
        ('CREFITO', 'CREFITO'),
        ('CRN', 'CRN'),
        ('CRF', 'CRF'),
        ('CRO', 'CRO'),
        ('CREFONO', 'CREFONO'),
        ('CRBM', 'CRBM'),
        ('CRMV', 'CRMV'),
        ('CREF', 'CREF'),
    ]

    CATEGORIA_CHOICES = [
        ('CLT', 'CLT'),
        ('PJ', 'PJ'),
        ('Autônomo', 'Autônomo'),
    ]

    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    conselho = models.CharField(max_length=20, choices=CONSELHOS_CHOICES)  # Obrigatório
    numero_conselho = models.CharField(max_length=20)  # Número + UF, ex: 123456-SP
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, blank=True, null=True)
    cpf_cnpj = models.CharField(max_length=20, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    endereco = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} - {self.especialidade}"
