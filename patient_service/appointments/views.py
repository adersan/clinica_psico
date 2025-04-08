# appointments/views.py

from rest_framework import generics
from .models import Consulta
from .serializers import ConsultaSerializer

class ConsultaListCreateView(generics.ListCreateAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

class ConsultaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
