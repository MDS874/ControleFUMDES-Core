from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nome', 'matricula', 'cpf', 'email', 'password']

    def create(self, validated_data):
        # Cria o usuário com senha criptografada
        user = User.objects.create_user(**validated_data)
        return user
