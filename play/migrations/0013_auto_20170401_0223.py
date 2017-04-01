# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0012_jogador_num_jogadas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogador',
            name='pontos',
            field=models.IntegerField(default=0),
        ),
    ]
