
from rest_framework import serializers
from .models import Paciente, Endereco

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'

class PacienteSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer(required=False, allow_null=True)

    class Meta:
        model = Paciente
        fields = '__all__'

    def create(self, validated_data):
        endereco_data = validated_data.pop('endereco', None)
        if endereco_data:
            endereco = Endereco.objects.create(**endereco_data)
            validated_data['endereco'] = endereco
        return Paciente.objects.create(**validated_data)

    def update(self, instance, validated_data):
        endereco_data = validated_data.pop('endereco', None)
        if endereco_data:
            endereco = instance.endereco
            if endereco:
                for attr, value in endereco_data.items():
                    setattr(endereco, attr, value)
                endereco.save()
            else:
                endereco = Endereco.objects.create(**endereco_data)
                instance.endereco = endereco

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
