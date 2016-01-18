# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mecze', '0027_auto_20151219_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mecz',
            name='id_skladu_goscia',
            field=models.ForeignKey(blank=True, related_name='sklad_goscia', verbose_name='Sklad goscia', to='Mecze.Sklad', null=True),
        ),
        migrations.AlterField(
            model_name='mecz',
            name='id_skladu_gospodarza',
            field=models.ForeignKey(blank=True, related_name='sklad_gospodarz', verbose_name='Sklad gospodarza', to='Mecze.Sklad', null=True),
        ),
    ]
