# appointments/views.py

from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Consulta
from .serializers import ConsultaSerializer
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_agendamentos(request):
    return render(request, 'appointments/dashboard_agendamentos.html')


class ConsultaListCreateView(generics.ListCreateAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # filtros exatos
    filterset_fields = ['data', 'status', 'paciente', 'profissional']

    # busca textual
    search_fields = ['paciente__nome', 'profissional__username']

    # ordenação
    ordering_fields = ['data', 'hora', 'status']

class ConsultaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
