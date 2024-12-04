from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Comprovante, Aluno, ComprovanteComentario
import base64
from .serializers import ComprovanteSerializer, ComprovanteComentarioSerializer

@api_view(['POST'])
def enviar_comprovante(request):
    try:
        # Recuperar os dados do formulário
        data = request.data

        # Ler o arquivo PDF como dados binários
        comprovante_file = request.FILES.get('comprovante')

        if not comprovante_file:
            return Response({"message": "Comprovante não fornecido."}, status=400)

        # Buscar a instância do Aluno
        try:
            aluno = Aluno.objects.get(id=data['idAluno'])
        except Aluno.DoesNotExist:
            return Response({"message": "Aluno não encontrado."}, status=404)

        # Salvar o arquivo PDF como dados binários
        comprovante_data = comprovante_file.read()  # Lê o arquivo como dados binários

        # Criar o objeto Comprovante
        comprovante = Comprovante.objects.create(
            idAluno=aluno,  # Atribuir a instância do Aluno
            data=data['data'],
            horas_prestadas=data['horas_prestadas'],
            local=data['local'],
            supervisor=data['supervisor'],
            comprovante=comprovante_data,  # Salvar o arquivo PDF como dados binários
            status=0  # Status default
        )

        # Retornar a resposta de sucesso
        return Response({"message": "Comprovante enviado com sucesso."}, status=201)

    except Exception as e:
        return Response({"message": str(e)}, status=400)

@api_view(['GET'])
def listar_comprovantes(request):
    try:
        # Obter o nome do aluno do query param
        nome_aluno = request.query_params.get('nome_aluno', None)

        # Obter todos os comprovantes com relação ao modelo core_aluno
        comprovantes = Comprovante.objects.select_related('idAluno').prefetch_related('comentarios').all()

        # Aplicar filtro se nome_aluno for fornecido
        if nome_aluno:
            comprovantes = comprovantes.filter(idAluno__nome=nome_aluno)

        # Serializar os dados e incluir o nome do aluno e os comentários
        serialized_data = [
            {
                "id": comprovante.id,
                "data": comprovante.data,
                "horas_prestadas": comprovante.horas_prestadas,
                "local": comprovante.local,
                "supervisor": comprovante.supervisor,
                "status": comprovante.status,
                "nome_aluno": comprovante.idAluno.nome,
                "comentarios": [
                    {
                        "id": comentario.id,
                        "comentario": comentario.texto,
                        "data": comentario.data_comentario
                    }
                    for comentario in comprovante.comentarios.all()
                ]
            }
            for comprovante in comprovantes
        ]

        return Response(serialized_data, status=200)
    except Exception as e:
        return Response({"error": str(e)}, status=400)

@api_view(['GET'])
def detalhes_comprovante(request, id):
    try:
        # Obter o comprovante pelo ID com o relacionamento com core_aluno
        comprovante = Comprovante.objects.select_related('idAluno').get(id=id)

        # Codificar o PDF em base64
        comprovante_base64 = base64.b64encode(comprovante.comprovante).decode('utf-8')

        # Retornar os dados, incluindo o nome do aluno
        return Response({
            "id": comprovante.id,
            "data": comprovante.data,
            "horas_prestadas": comprovante.horas_prestadas,
            "local": comprovante.local,
            "supervisor": comprovante.supervisor,
            "status": comprovante.status,
            "nome_aluno": comprovante.idAluno.nome,  # Nome do aluno
            "comprovante": comprovante_base64,  # Envia o PDF em base64
        }, status=200)
    except Comprovante.DoesNotExist:
        return Response({"error": "Comprovante não encontrado."}, status=404)
    except Exception as e:
        return Response({"error": str(e)}, status=400)

class ComentarComprovanteView(APIView):
    def post(self, request):
        serializer = ComprovanteComentarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Comentário registrado com sucesso."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def get_comentarios_comprovante(request, comprovante_id):
    comentarios = ComprovanteComentario.objects.filter(id_comprovante=comprovante_id)
    comentarios_data = [{"comentario": c.comentario, "status": c.status} for c in comentarios]
    return Response(comentarios_data, safe=False)
