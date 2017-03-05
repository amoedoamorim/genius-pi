# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0003_auto_20170305_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='campeonato',
            name='dificuldade',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='campeonato',
            name='velocidade',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
