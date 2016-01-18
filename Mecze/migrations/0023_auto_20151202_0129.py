# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mecze', '0022_auto_20151202_0125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mecz',
            name='id_wyniku',
        ),
        migrations.AddField(
            model_name='mecz',
            name='gole_goscia',
            field=models.IntegerField(),
        ),
        migrations.AddField(
            model_name='mecz',
            name='gole_gospodarza',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Wynik',
        ),
    ]
