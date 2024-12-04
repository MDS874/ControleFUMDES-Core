from rest_framework import serializers
from .models import Comprovante, ComprovanteComentario

class ComprovanteSerializer(serializers.ModelSerializer):
    nome_aluno = serializers.CharField(source="aluno.nome", read_only=True)  # Campo do nome do aluno

    class Meta:
        model = Comprovante
        fields = ['id', 'data', 'horas_prestadas', 'local', 'supervisor', 'status', 'nome_aluno']


class ComprovanteComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComprovanteComentario
        fields = ['id_comprovante', 'comentario', 'status']

    def validate(self, data):
        if data['status'] == 2 and not data['comentario']:
            raise serializers.ValidationError("Não é possível rejeitar sem comentário.")
        return data

    def create(self, validated_data):
        # Atualiza o status do comprovante
        comprovante = validated_data['id_comprovante']
        comprovante.status = validated_data['status']
        comprovante.save()

        # Cria o comentário
        return ComprovanteComentario.objects.create(**validated_data)
        
class ComprovanteComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComprovanteComentario
        fields = ['id', 'comentario', 'status', 'data_comentario']