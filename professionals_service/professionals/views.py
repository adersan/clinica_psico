from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Profissional
from .serializers import ProfissionalSerializer

class ProfissionalListCreateView(generics.ListCreateAPIView):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer
    permission_classes = [IsAuthenticated]

class ProfissionalRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer
    permission_classes = [IsAuthenticated]
