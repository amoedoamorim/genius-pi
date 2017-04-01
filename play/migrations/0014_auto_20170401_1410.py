# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0013_auto_20170401_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogador',
            name='tempo',
            field=models.DecimalField(null=True, decimal_places=3, max_digits=10),
        ),
    ]
