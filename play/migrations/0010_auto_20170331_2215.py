# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0009_auto_20170331_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campeonato',
            name='dificuldade',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='campeonato',
            name='num_rounds',
            field=models.PositiveIntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='campeonato',
            name='velocidade',
            field=models.PositiveIntegerField(),
        ),
    ]
