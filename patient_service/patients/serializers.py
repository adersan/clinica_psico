from rest_framework import serializers
from .models import Paciente, Endereco
import re
from datetime import date


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'


class PacienteSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()

    class Meta:
        model = Paciente
        fields = '__all__'

    def validate_cpf(self, value):
        cpf = re.sub(r'\D', '', value)
        if len(cpf) != 11 or not cpf.isdigit():
            raise serializers.ValidationError("CPF inválido.")
        return value

    def validate_email(self, value):
        if self.instance:
            if Paciente.objects.filter(email=value).exclude(pk=self.instance.pk).exists():
                raise serializers.ValidationError("Este email já está cadastrado.")
        else:
            if Paciente.objects.filter(email=value).exists():
                raise serializers.ValidationError("Este email já está cadastrado.")
        return value

    def validate_data_nascimento(self, value):
        if value >= date.today():
            raise serializers.ValidationError("A data de nascimento deve ser no passado.")
        return value

    def validate_telefone(self, value):
        if not re.match(r'^\(\d{2}\) \d{4,5}-\d{4}$', value):
            raise serializers.ValidationError("Formato de telefone inválido. Use o padrão (XX) XXXXX-XXXX.")
        return value

    def create(self, validated_data):
        endereco_data = validated_data.pop('endereco')
        endereco = Endereco.objects.create(**endereco_data)
        paciente = Paciente.objects.create(endereco=endereco, **validated_data)
        return paciente

    def update(self, instance, validated_data):
        endereco_data = validated_data.pop('endereco', None)
        if endereco_data:
            for attr, value in endereco_data.items():
                setattr(instance.endereco, attr, value)
            instance.endereco.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
