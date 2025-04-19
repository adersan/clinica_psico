# notifications/views.py
import requests
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Notificacao
from .serializers import NotificacaoSerializer
from django.core.mail import send_mail
from django.conf import settings

# Função auxiliar para envio de e-mail
def enviar_email(destino, assunto, mensagem):
    try:
        send_mail(
            subject=assunto,
            message=mensagem,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[destino],
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(f"[ERRO EMAIL]: {e}")
        return False


# Listagem e criação de notificações
class NotificacaoListCreateView(generics.ListCreateAPIView):
    queryset = Notificacao.objects.all()
    serializer_class = NotificacaoSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        notificacao = serializer.save()

        if notificacao.tipo == "email":
            sucesso = enviar_email(
                destino=notificacao.destino,
                assunto=notificacao.assunto or "Clínica PSICO+",
                mensagem=notificacao.mensagem
            )
            if sucesso:
                notificacao.enviada = True
                notificacao.save()


# Detalhes, atualização e exclusão
class NotificacaoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notificacao.objects.all()
    serializer_class = NotificacaoSerializer
    permission_classes = [IsAuthenticated]


# Envio específico via WhatsApp (WAHA)
class EnviarWhatsappView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        numero = request.data.get("numero")
        mensagem = request.data.get("mensagem")

        if not numero or not mensagem:
            return Response(
                {"error": "Número e mensagem são obrigatórios."},
                status=status.HTTP_400_BAD_REQUEST
            )

        payload = {
            "phone": numero,
            "message": mensagem
        }

        try:
            response = requests.post(
                url="http://localhost:3000/sendMessage",
                json=payload,
                timeout=10
            )

            if response.status_code == 200:
                return Response({"success": "Mensagem enviada com sucesso via WAHA."})
            else:
                return Response({
                    "error": "Erro ao enviar via WAHA.",
                    "detail": response.text
                }, status=response.status_code)

        except requests.exceptions.RequestException as e:
            return Response({
                "error": "Erro de conexão com WAHA.",
                "detail": str(e)
            }, status=status.HTTP_502_BAD_GATEWAY)
