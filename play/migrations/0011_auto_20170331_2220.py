# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0010_auto_20170331_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campeonato',
            name='dificuldade',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(5)], default=10),
        ),
        migrations.AlterField(
            model_name='campeonato',
            name='num_rounds',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)], default=3),
        ),
        migrations.AlterField(
            model_name='campeonato',
            name='velocidade',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)], default=4),
        ),
    ]
