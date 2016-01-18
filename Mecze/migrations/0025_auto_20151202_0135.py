# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mecze', '0024_auto_20151202_0132'),
    ]

    operations = [
        migrations.AddField(
            model_name='mecz',
            name='gole_goscia',
            field=models.CharField(default=2, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mecz',
            name='gole_gospodarza',
            field=models.CharField(default=3, max_length=2),
            preserve_default=False,
        ),
    ]
