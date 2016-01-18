# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mecze', '0025_auto_20151202_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mecz',
            name='gole_goscia',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='mecz',
            name='gole_gospodarza',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='mecz',
            name='id_goscia',
            field=models.ForeignKey(to='Mecze.Zespol', related_name='mecz_gosc', verbose_name='Gosc'),
        ),
        migrations.AlterField(
            model_name='mecz',
            name='id_gospodarza',
            field=models.ForeignKey(to='Mecze.Zespol', related_name='mecz_gospodarz', verbose_name='Gospodarz'),
        ),
        migrations.AlterField(
            model_name='mecz',
            name='id_kolejki',
            field=models.ForeignKey(to='Mecze.Kolejka', verbose_name='Nr kolejki'),
        ),
        migrations.AlterField(
            model_name='mecz',
            name='id_skladu_goscia',
            field=models.ForeignKey(to='Mecze.Sklad', default='', blank=True, related_name='sklad_goscia', verbose_name='Sklad goscia'),
        ),
        migrations.AlterField(
            model_name='mecz',
            name='id_skladu_gospodarza',
            field=models.ForeignKey(to='Mecze.Sklad', default='', blank=True, related_name='sklad_gospodarz', verbose_name='Sklad gospodarza'),
        ),
        migrations.AlterField(
            model_name='mecz',
            name='uwagi',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
