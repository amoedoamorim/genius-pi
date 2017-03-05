from django.db import models
from django.utils import timezone

# Create your models here.
class Campeonato(models.Model):
    titulo = models.CharField(max_length=50)
    data = models.DateTimeField(default=timezone.now)
    dificuldade = models.IntegerField()
    velocidade = models.IntegerField()

    def __str__(self):
        return self.titulo

class Jogador(models.Model):
    nome = models.CharField(max_length=50)
    apelido = models.CharField(max_length=25)
    pontos =  models.IntegerField(blank=True, null=True)
    tempo = models.IntegerField(blank=True, null=True)
    campeonato = models.ForeignKey('Campeonato')

    def __str__(self):
        return self.apelido
