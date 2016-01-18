# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mecze', '0018_auto_20151202_0112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wynik',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('gole_gospodarza', models.IntegerField()),
                ('gole_goscia', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='mecz',
            name='id_wyniku',
            field=models.ForeignKey(to='Mecze.Wynik', default=''),
        ),
    ]
