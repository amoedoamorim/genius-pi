# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0014_auto_20170401_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogador',
            name='menor_tempo',
            field=models.DecimalField(decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='jogador',
            name='pontos_rodada',
            field=models.IntegerField(default=0),
        ),
    ]
