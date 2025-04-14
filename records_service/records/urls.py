# records/urls.py

from django.urls import path
from .views import RecordListCreateView

urlpatterns = [
    path('records/', RecordListCreateView.as_view(), name='record-list-create'),
]
