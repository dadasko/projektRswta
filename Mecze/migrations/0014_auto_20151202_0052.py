# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mecze', '0013_auto_20151202_0044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sklad_na_mecz',
            name='id_meczu',
        ),
        migrations.RemoveField(
            model_name='sklad_na_mecz',
            name='id_skladu',
        ),
        migrations.RemoveField(
            model_name='sklad_na_mecz',
            name='id_zespolu',
        ),
        migrations.AlterField(
            model_name='mecz',
            name='id_skladu_goscia',
            field=models.ForeignKey(default='', to='Mecze.Sklad', related_name='sklad_goscia'),
        ),
        migrations.AlterField(
            model_name='mecz',
            name='id_skladu_gospodarza',
            field=models.ForeignKey(default='', to='Mecze.Sklad', related_name='sklad_gospodarz'),
        ),
        migrations.DeleteModel(
            name='Sklad_na_mecz',
        ),
    ]
