from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True, default=0)
    curso = models.CharField(max_length=100)
    horas_devidas = models.IntegerField(default=120)
    horas_cumpridas = models.IntegerField(default=0)

    def __str__(self):
        return self.nome
