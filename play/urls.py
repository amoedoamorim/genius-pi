from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^campeonato/(?P<pk>[0-9]+)/$', views.campeonato),
    url(r'^campeonato/(?P<pk>[0-9]+)\.json$', views.campeonato_json),
    url(r'^campeonato/new/$', views.campeonato_new, name='campeonato_new'),
    url(r'^jogador/new/$', views.jogador_new, name='jogador_new'),
    url(r'^partida', views.partida, name='partida'),
]
