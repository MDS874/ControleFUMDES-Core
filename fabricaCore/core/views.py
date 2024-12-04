from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.response import Response
from .models import Aluno

class AlunoListAPIView(APIView):
    def get(self, request):
        alunos = Aluno.objects.all().values('id', 'nome', 'curso', 'horas_devidas', 'horas_cumpridas')
        return Response(list(alunos))

class CustomTokenObtainPairView(TokenObtainPairView):
    # Essa view vai gerar o access_token e refresh_token
    pass
