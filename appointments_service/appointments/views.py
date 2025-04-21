from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Consulta
from .serializers import ConsultaSerializer

class ConsultaListCreateView(generics.ListCreateAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    permission_classes = [IsAuthenticated]

class ConsultaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    permission_classes = [IsAuthenticated]
