# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0002_jogador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogador',
            name='pontos',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jogador',
            name='tempo',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
