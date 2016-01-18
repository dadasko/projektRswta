# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mecze', '0019_auto_20151202_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wynik',
            name='gole_goscia',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='wynik',
            name='gole_gospodarza',
            field=models.CharField(max_length=2),
        ),
    ]
