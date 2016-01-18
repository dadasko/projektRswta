# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mecze', '0020_auto_20151202_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mecz',
            name='id_wyniku',
            field=models.ForeignKey(to='Mecze.Wynik'),
        ),
    ]
