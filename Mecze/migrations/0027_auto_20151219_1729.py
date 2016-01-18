# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mecze', '0026_auto_20151219_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mecz',
            name='id_skladu_goscia',
            field=models.ForeignKey(related_name='sklad_goscia', to='Mecze.Sklad', default='', verbose_name='Sklad goscia', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='mecz',
            name='id_skladu_gospodarza',
            field=models.ForeignKey(related_name='sklad_gospodarz', to='Mecze.Sklad', default='', verbose_name='Sklad gospodarza', null=True, blank=True),
        ),
    ]
