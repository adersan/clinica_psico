
from rest_framework import serializers
from .models import Consulta

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'

    def validate(self, data):
        profissional = data.get('profissional')
        data_consulta = data.get('data')
        hora_consulta = data.get('hora')

        if self.instance:
            conflitos = Consulta.objects.filter(
                profissional=profissional,
                data=data_consulta,
                hora=hora_consulta
            ).exclude(pk=self.instance.pk)
        else:
            conflitos = Consulta.objects.filter(
                profissional=profissional,
                data=data_consulta,
                hora=hora_consulta
            )

        if conflitos.exists():
            raise serializers.ValidationError("Já existe uma consulta marcada com este profissional neste horário.")

        return data
