from rest_framework import generics, status, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from .models import Paciente
from .serializers import PacienteSerializer

# LISTAR e CRIAR pacientes
class PatientListCreateView(generics.ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['nome', 'cpf', 'endereco__cidade']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            "message": "Paciente criado com sucesso!",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)


# OBTER, ATUALIZAR e DELETAR paciente específico
class PatientRetrieveUpdateDestroyView(APIView):
    def get(self, request, pk):
        paciente = get_object_or_404(Paciente, pk=pk)
        serializer = PacienteSerializer(paciente)
        return Response(serializer.data)

    def put(self, request, pk):
        paciente = get_object_or_404(Paciente, pk=pk)
        serializer = PacienteSerializer(paciente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Paciente atualizado com sucesso!",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        paciente = get_object_or_404(Paciente, pk=pk)
        paciente.delete()
        return Response({
            "message": "Paciente deletado com sucesso!"
        }, status=status.HTTP_200_OK)
