# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0008_campeonato_num_rounds'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campeonato',
            name='num_rounds',
            field=models.IntegerField(default=3),
        ),
    ]
