# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0011_auto_20170331_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogador',
            name='num_jogadas',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
