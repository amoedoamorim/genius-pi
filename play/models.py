from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator

# Create your models here.
class Campeonato(models.Model):
    titulo = models.CharField(max_length=50)
    data = models.DateTimeField(default=timezone.now)
    dificuldade = models.PositiveIntegerField(default=10, validators=[MinValueValidator(5)])
    velocidade = models.PositiveIntegerField(default=4, validators=[MinValueValidator(1)])
    num_rounds = models.PositiveIntegerField(default=3, validators=[MinValueValidator(1)])
    jogador1_id = models.IntegerField(blank=True, null=True)
    jogador2_id = models.IntegerField(blank=True, null=True)
    vencedor_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.titulo

    def jogador1(self):
        return Jogador.objects.get(id=self.jogador1_id)

    def jogador2(self):
        return Jogador.objects.get(id=self.jogador2_id)

    def get_vencedor(self):
        if self.vencedor_id:
            return Jogador.objects.get(id=self.vencedor_id)

        if (not self.jogador1_id or not self.jogador2_id):
            return None

        jogador1 = self.jogador1()
        jogador2 = self.jogador2()

        if (jogador2.num_jogadas == self.num_rounds):
            if (jogador1.pontos == jogador2.pontos):
                self.num_rounds += 1
                self.save()
            else:
                if (jogador1.pontos > jogador2.pontos):
                    self.vencedor_id = jogador1.pk
                else:
                    self.vencedor_id = jogador2.pk
                self.save()
        else:
            return None

    def get_jogador_vez(self):
        if self.vencedor_id:
            return None
        else:
            if (self.jogador1().num_jogadas == self.jogador2().num_jogadas):
                return self.jogador1()
            else:
                return self.jogador2()

class Jogador(models.Model):
    nome = models.CharField(max_length=50)
    apelido = models.CharField(max_length=25)
    num_jogadas = models.PositiveIntegerField(default=0)
    pontos = models.IntegerField(default=0)
    pontos_rodada = models.IntegerField(default=0)
    tempo = models.DecimalField(default=0, max_digits=10, decimal_places=3)
    menor_tempo = models.DecimalField(default=0, max_digits=10, decimal_places=3)

    def __str__(self):
        return self.apelido
