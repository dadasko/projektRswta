# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mecze', '0017_auto_20151202_0109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mecz',
            name='gole_goscia',
        ),
        migrations.RemoveField(
            model_name='mecz',
            name='gole_gospodarza',
        ),
    ]
