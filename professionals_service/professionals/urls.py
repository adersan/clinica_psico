from django.urls import path
from .views import ProfissionalListCreateView, ProfissionalRetrieveUpdateDestroyView

urlpatterns = [
    path('', ProfissionalListCreateView.as_view(), name='profissionais-list-create'),
    path('<int:pk>/', ProfissionalRetrieveUpdateDestroyView.as_view(), name='profissionais-detail'),
]
