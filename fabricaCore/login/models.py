from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# Criar um Gerenciador de Usuários Personalizado
class UserManager(BaseUserManager):
    def create_user(self, cpf, password, **extra_fields):
        if not cpf:
            raise ValueError('O CPF deve ser fornecido')
        user = self.model(cpf=cpf, password=password, **extra_fields)
        user.set_password(password)  # Criptografa a senha
        user.save(using=self._db)
        return user

    def create_superuser(self, cpf, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(cpf, password, **extra_fields)

# Criar o Modelo de Usuário Personalizado
class User(AbstractBaseUser):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    # Campos adicionais
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Permite acesso ao admin
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'cpf'  # Usar o CPF para login
    REQUIRED_FIELDS = ['nome', 'matricula', 'email']

    def __str__(self):
        return self.nome
