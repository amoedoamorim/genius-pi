# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0005_campeonato_vencedor_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='campeonato',
            name='jogador1_id',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='campeonato',
            name='jogador2_id',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
