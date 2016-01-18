# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mecze', '0014_auto_20151202_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='sklad',
            name='nazwa_skladu',
            field=models.CharField(default='', max_length=32),
        ),
    ]
