from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import UserProfile

# Dashboard de agendamentos
@login_required(login_url='/login/')
def dashboard_agendamentos(request):
    return render(request, 'authentication/dashboard_agendamentos.html')

# Dashboard de pacientes
@login_required(login_url='/login/')
def dashboard_pacientes(request):
    return render(request, 'authentication/dashboard_pacientes.html')

# Tela de login com validação
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'authentication/login.html', {'error': 'Usuário ou senha inválidos'})

    return render(request, 'authentication/login.html')

# Tela do dashboard padrão
@login_required(login_url='/login/')
def dashboard_view(request):
    return render(request, 'authentication/dashboard.html')

# Tela de cadastro de usuário visual (HTML)
def register_view(request):
    return render(request, 'authentication/register.html')

# View para autenticação baseada em template
class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'

# Página inicial
def home_view(request):
    return render(request, 'authentication/login.html')

# API de cadastro de usuários (aberta)
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        user_type = request.data.get('user_type', 'psicologo')

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Usuário já existe!'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name
        )

        UserProfile.objects.create(user=user, user_type=user_type)

        return Response({'message': 'Usuário criado com sucesso!'}, status=status.HTTP_201_CREATED)

# API de login com retorno do token JWT
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            return Response({'error': 'Credenciais inválidas!'}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        user_type = user.profile.user_type if hasattr(user, 'profile') else 'desconhecido'

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'username': user.username,
            'user_type': user_type
        })

# API de logout com blacklist do refresh token
class LogoutView(APIView):
    def post(self, request):
        refresh_token = request.data.get('refresh')

        if not refresh_token:
            return Response({'error': 'Token de refresh não enviado!'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': 'Logout realizado com sucesso!'}, status=status.HTTP_200_OK)
        except TokenError:
            return Response({'error': 'Token inválido ou já expirado!'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': f'Erro inesperado: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# View protegida para aprovação de usuários (somente admin)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def aprovar_usuarios_view(request):
    jwt_auth = JWTAuthentication()
    try:
        user, _ = jwt_auth.authenticate(request)
    except:
        return Response({'detail': 'Token inválido ou expirado'}, status=status.HTTP_401_UNAUTHORIZED)

    if not hasattr(user, 'profile') or user.profile.user_type != 'admin':
        return Response({'detail': 'Acesso negado. Apenas administradores podem acessar esta área.'}, status=status.HTTP_403_FORBIDDEN)

    return render(request, 'authentication/partials/aprovacao_parcial.html')
