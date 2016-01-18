# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mecze', '0004_remove_wynik_id_kolejki'),
    ]

    operations = [
        migrations.AddField(
            model_name='mecz',
            name='id_skladu_goscia',
            field=models.ForeignKey(default='', to='Mecze.Sklad_na_mecz', related_name='sklad_goscia'),
        ),
        migrations.AddField(
            model_name='mecz',
            name='id_skladu_gospodarza',
            field=models.ForeignKey(default='', to='Mecze.Sklad_na_mecz', related_name='sklad_gospodarz'),
        ),
    ]
