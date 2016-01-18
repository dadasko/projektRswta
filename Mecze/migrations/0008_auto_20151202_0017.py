# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mecze', '0007_auto_20151202_0016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mecz',
            name='id_skladu_goscia',
        ),
        migrations.RemoveField(
            model_name='mecz',
            name='id_skladu_gospodarza',
        ),
    ]
