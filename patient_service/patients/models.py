from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)

    # Importante: O campo endereco fica aqui por dependência do modelo Endereco.
    # Como Endereco ainda não foi definido, é necessário movê-lo para baixo
    # e usar uma string no relacionamento para evitar erro de referência circular
    endereco = models.OneToOneField('Endereco', on_delete=models.CASCADE, related_name='paciente')

    def __str__(self):
        return self.nome

class Endereco(models.Model):
    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=9)

    def __str__(self):
        return f'{self.rua}, {self.numero} - {self.cidade}/{self.estado}'
