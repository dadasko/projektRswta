# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mecze', '0016_auto_20151202_0108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mecz',
            name='gole_goscia',
            field=models.CharField(default='', max_length=2),
        ),
        migrations.AlterField(
            model_name='mecz',
            name='gole_gospodarza',
            field=models.CharField(default='', max_length=2),
        ),
    ]
