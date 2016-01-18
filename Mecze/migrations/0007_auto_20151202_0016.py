# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mecze', '0006_auto_20151202_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mecz',
            name='id_skladu_goscia',
            field=models.ForeignKey(related_name='sklad_goscia', blank=True, default='', to='Mecze.Sklad_na_mecz', null=True),
        ),
        migrations.AlterField(
            model_name='mecz',
            name='id_skladu_gospodarza',
            field=models.ForeignKey(related_name='sklad_gospodarz', blank=True, default='', to='Mecze.Sklad_na_mecz', null=True),
        ),
    ]
