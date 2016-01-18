# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mecze', '0002_zespol_opis'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wynik',
            name='id_meczu',
        ),
    ]
