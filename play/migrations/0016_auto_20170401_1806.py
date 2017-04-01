# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0015_auto_20170401_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogador',
            name='menor_tempo',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='jogador',
            name='tempo',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
        ),
    ]
