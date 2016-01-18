# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mecze', '0005_auto_20151202_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mecz',
            name='id_skladu_goscia',
            field=models.ForeignKey(null=True, default='', to='Mecze.Sklad_na_mecz', related_name='sklad_goscia'),
        ),
        migrations.AlterField(
            model_name='mecz',
            name='id_skladu_gospodarza',
            field=models.ForeignKey(null=True, default='', to='Mecze.Sklad_na_mecz', related_name='sklad_gospodarz'),
        ),
    ]
