from django import forms
from .models import Campeonato
from .models import Jogador

class CampeonatoForm(forms.ModelForm):

    class Meta:
        model = Campeonato
        fields = ('titulo', 'dificuldade', 'velocidade')

class JogadorForm(forms.ModelForm):

    class Meta:
        model = Jogador
        fields = ('nome', 'apelido')
