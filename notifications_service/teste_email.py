import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notifications_service.settings')
django.setup()

from django.core.mail import send_mail

send_mail(
    'Teste de E-mail',
    'Este é um teste de envio do Django com Gmail.',
    'adersan@hotmail.com',
    ['adersan@hotmail.com'],
    fail_silently=False,
)
print("E-mail enviado com sucesso!")
#         mensagem = request.data.get("mensagem")