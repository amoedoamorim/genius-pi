from django import forms
from .models import Campeonato
from .models import Jogador

class CampeonatoForm(forms.ModelForm):

    class Meta:
        model = Campeonato
        fields = ('titulo', 'dificuldade', 'velocidade', 'num_rounds')

class JogadorForm(forms.ModelForm):

    class Meta:
        model = Jogador
        fields = ('nome', 'apelido')
