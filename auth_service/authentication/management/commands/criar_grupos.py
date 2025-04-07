from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = 'Cria os grupos padrão do sistema'

    def handle(self, *args, **kwargs):
        grupos = ['Admin', 'Psicólogo', 'Recepcionista', 'Paciente']
        for nome in grupos:
            group, created = Group.objects.get_or_create(name=nome)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Grupo "{nome}" criado com sucesso.'))
            else:
                self.stdout.write(self.style.WARNING(f'Grupo "{nome}" já existe.'))
