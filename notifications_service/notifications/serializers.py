# notifications/serializers.py

from rest_framework import serializers
from .models import Notificacao

class NotificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacao
        fields = '__all__'

    def validate(self, data):
        tipo = data.get('tipo')
        destino = data.get('destino')

        if tipo == 'email':
            if '@' not in destino:
                raise serializers.ValidationError({'destino': 'Endereço de e-mail inválido.'})
        elif tipo == 'sms':
            if not destino.isdigit() or len(destino) < 10:
                raise serializers.ValidationError({'destino': 'Número de telefone inválido para SMS.'})
        elif tipo == 'whatsapp':
            if not destino.startswith('+') or not destino[1:].isdigit():
                raise serializers.ValidationError({'destino': 'Número de WhatsApp inválido. Ex: +5511999999999'})

        return data
