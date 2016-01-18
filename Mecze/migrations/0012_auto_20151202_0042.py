# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mecze', '0011_auto_20151202_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='sklad',
            name='id_pozycji',
            field=models.ForeignKey(to='Mecze.Pozycja', default=''),
        ),
        migrations.AddField(
            model_name='sklad',
            name='id_zawodnika',
            field=models.ForeignKey(to='Mecze.Zawodnik', default=''),
        ),
    ]
