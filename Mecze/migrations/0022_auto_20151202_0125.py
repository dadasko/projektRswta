# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mecze', '0021_auto_20151202_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sklad',
            name='nazwa_skladu',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='wynik',
            name='gole_goscia',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='wynik',
            name='gole_gospodarza',
            field=models.IntegerField(),
        ),
    ]
