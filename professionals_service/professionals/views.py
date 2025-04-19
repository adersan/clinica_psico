from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Profissional
from .serializers import ProfissionalSerializer


class ProfissionalListCreateView(generics.ListCreateAPIView):
    """
    GET: Lista todos os profissionais
    POST: Cria um novo profissional
    """
    queryset = Profissional.objects.all().order_by('nome')
    serializer_class = ProfissionalSerializer
    permission_classes = [IsAuthenticated]


class ProfissionalRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Recupera um profissional específico
    PUT/PATCH: Atualiza dados do profissional
    DELETE: Remove o profissional
    """
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer
    permission_classes = [IsAuthenticated]
