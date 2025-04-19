from rest_framework import serializers
from .models import Profissional
import re


class ProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profissional
        fields = '__all__'

    def validate_conselho(self, value):
        if value == "":
            raise serializers.ValidationError("Selecione um conselho válido.")
        return value

    def validate_numero_conselho(self, value):
        if not re.match(r'^\d{4,6}-[A-Z]{2}$', value):
            raise serializers.ValidationError("Número do conselho deve estar no formato 123456-SP.")
        return value

    def validate_email(self, value):
        if Profissional.objects.filter(email=value).exclude(pk=self.instance.pk if self.instance else None).exists():
            raise serializers.ValidationError("Este e-mail já está cadastrado.")
        return value

    def validate(self, data):
        obrigatorios = ['nome', 'especialidade', 'telefone', 'email', 'conselho', 'numero_conselho']
        for campo in obrigatorios:
            if not data.get(campo):
                raise serializers.ValidationError({campo: "Este campo é obrigatório."})
        return data
