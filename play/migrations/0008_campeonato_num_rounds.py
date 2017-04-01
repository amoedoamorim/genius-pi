# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0007_remove_jogador_campeonato'),
    ]

    operations = [
        migrations.AddField(
            model_name='campeonato',
            name='num_rounds',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]
