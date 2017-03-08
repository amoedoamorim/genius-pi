# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0006_auto_20170305_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jogador',
            name='campeonato',
        ),
    ]
