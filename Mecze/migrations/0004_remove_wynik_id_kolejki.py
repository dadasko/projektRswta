# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mecze', '0003_remove_wynik_id_meczu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wynik',
            name='id_kolejki',
        ),
    ]
