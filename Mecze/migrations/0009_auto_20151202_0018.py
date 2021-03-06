# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mecze', '0008_auto_20151202_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='mecz',
            name='id_skladu_goscia',
            field=models.ForeignKey(default='', to='Mecze.Sklad_na_mecz', related_name='sklad_goscia', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='mecz',
            name='id_skladu_gospodarza',
            field=models.ForeignKey(default='', to='Mecze.Sklad_na_mecz', related_name='sklad_gospodarz', null=True, blank=True),
        ),
    ]
