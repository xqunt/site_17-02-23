from django.db import models
from uuid import uuid4

class Postagem(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo