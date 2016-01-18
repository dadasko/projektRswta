# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mecze', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zespol',
            name='opis',
            field=models.CharField(default='', max_length=256),
        ),
    ]
