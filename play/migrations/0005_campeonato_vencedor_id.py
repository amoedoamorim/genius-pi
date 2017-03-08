# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0004_auto_20170305_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='campeonato',
            name='vencedor_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
