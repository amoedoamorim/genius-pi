# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jogador',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('apelido', models.CharField(max_length=25)),
                ('pontos', models.IntegerField()),
                ('tempo', models.IntegerField()),
                ('campeonato', models.ForeignKey(to='play.Campeonato')),
            ],
        ),
    ]
