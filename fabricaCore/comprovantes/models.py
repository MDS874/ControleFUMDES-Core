from django.db import models
from core.models import Aluno  # Importe o modelo do app correto

class Comprovante(models.Model):
    PENDENTE = 0
    APROVADO = 1
    REPROVADO = 2

    STATUS_CHOICES = [
        (PENDENTE, 'Pendente'),
        (APROVADO, 'Aprovado'),
        (REPROVADO, 'Reprovado'),
    ]
    
    idAluno = models.ForeignKey(
        Aluno,  # Referência ao modelo core.Aluno
        on_delete=models.CASCADE,
        db_column='idAluno'
    )
    data = models.DateField()
    horas_prestadas = models.IntegerField()
    local = models.CharField(max_length=255)
    supervisor = models.CharField(max_length=255)
    comprovante = models.BinaryField() 
    status = models.IntegerField(default=0, choices=STATUS_CHOICES)  # 0 significa que está pendente de aprovação

    def __str__(self):
        return f"Comprovante de {self.idAluno} - Status: {self.status}"

class ComprovanteComentario(models.Model):
    id = models.AutoField(primary_key=True)
    data_comentario = models.DateTimeField(auto_now_add=True)
    id_comprovante = models.ForeignKey(Comprovante, on_delete=models.CASCADE, related_name="comentarios")
    texto = models.TextField()  # Altere para 'texto' se necessário
    status = models.IntegerField(choices=[(1, 'Aprovado'), (2, 'Rejeitado')])

    def __str__(self):
        return f"Comentário sobre {self.id_comprovante.id} - Status: {self.status}"
