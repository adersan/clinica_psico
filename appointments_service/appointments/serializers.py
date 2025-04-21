from rest_framework import serializers
from .models import Consulta

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'

    def validate(self, data):
        profissional_id = data.get('profissional_id')
        data_consulta = data.get('data')
        hora_consulta = data.get('hora')

        conflitos = Consulta.objects.filter(
            profissional_id=profissional_id,
            data=data_consulta,
            hora=hora_consulta
)


        if self.instance:
            conflitos = conflitos.exclude(pk=self.instance.pk)

        if conflitos.exists():
            raise serializers.ValidationError("Já existe uma consulta marcada com este profissional neste horário.")

        return data
