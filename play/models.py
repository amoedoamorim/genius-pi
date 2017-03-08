from django.db import models
from django.utils import timezone

# Create your models here.
class Campeonato(models.Model):
    titulo = models.CharField(max_length=50)
    data = models.DateTimeField(default=timezone.now)
    dificuldade = models.IntegerField()
    velocidade = models.IntegerField()
    jogador1_id = models.IntegerField(blank=True, null=True)
    jogador2_id = models.IntegerField(blank=True, null=True)
    vencedor_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.titulo

    def jogador1(self):
        return Jogador.objects.get(id=self.jogador1_id)

    def jogador2(self):
        return Jogador.objects.get(id=self.jogador2_id)

class Jogador(models.Model):
    nome = models.CharField(max_length=50)
    apelido = models.CharField(max_length=25)
    pontos =  models.IntegerField(blank=True, null=True)
    tempo = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.apelido
