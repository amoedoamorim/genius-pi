from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .forms import CampeonatoForm, JogadorForm
from .models import Campeonato, Jogador
import subprocess

def home(request):
    campeonatosPassados = Campeonato.objects.all().exclude(vencedor_id = None)
    campeonatoAtual = Campeonato.objects.filter(vencedor_id = None).last()

    if (campeonatoAtual):
        return redirect('play.views.campeonato', pk = campeonatoAtual.pk)

    return render(request, 'play/home.html', {'campeonatosPassados': campeonatosPassados, 'campeonatoAtual': campeonatoAtual})

def campeonato(request, pk):
    campeonato = Campeonato.objects.get(pk = pk)

    if campeonato.vencedor_id:
        vencedor = Jogador.objects.get(pk = campeonato.vencedor_id)
    else:
        vencedor = None;

    return render(request, 'play/campeonato.html', {'campeonato': campeonato, 'vencedor': vencedor})

def campeonato_json(request, pk):
    campeonato = Campeonato.objects.get(pk = pk)

    data = {
        'nome': campeonato.titulo,
        'data': campeonato.data
    }
    return JsonResponse(data)

def campeonato_new(request):
    if request.method == "POST":
        form = CampeonatoForm(request.POST)
        if form.is_valid():
            campeonato = form.save(commit = False)
            campeonato.data = timezone.now()
            campeonato.save()
            return redirect('play.views.campeonato', pk = campeonato.pk)
    else:
        form = CampeonatoForm()
    return render(request, 'play/campeonato_new.html', {'form': form})

def jogador_new(request):
    if request.method == "POST":
        campeonatoAtual = Campeonato.objects.filter(vencedor_id = None).last()

        form = JogadorForm(request.POST)
        if form.is_valid():
            jogador = form.save(commit = False)
            jogador.save()

            if not (campeonatoAtual.jogador1_id):
                campeonatoAtual.jogador1_id = jogador.pk

            elif not (campeonatoAtual.jogador2_id):
                campeonatoAtual.jogador2_id = jogador.pk

            campeonatoAtual.save()

            return redirect('play.views.campeonato', pk = campeonatoAtual.pk)
    else:
        form = JogadorForm()
    return render(request, 'play/jogador_new.html', {'form': form})

def partida(request):
    process = subprocess.Popen(['python', '/home/alexandre/workspace/genius-pi/play/teste.py'])
    return JsonResponse({'partida': 'sucesso'})
