# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mecze', '0012_auto_20151202_0042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sklad',
            name='id_pozycji',
        ),
        migrations.RemoveField(
            model_name='sklad',
            name='id_zawodnika',
        ),
        migrations.AddField(
            model_name='sklad',
            name='pozycja_1',
            field=models.ForeignKey(to='Mecze.Pozycja', default='', related_name='zp1'),
        ),
        migrations.AddField(
            model_name='sklad',
            name='pozycja_10',
            field=models.ForeignKey(to='Mecze.Pozycja', default='', related_name='zp10'),
        ),
        migrations.AddField(
            model_name='sklad',
            name='pozycja_11',
            field=models.ForeignKey(to='Mecze.Pozycja', default='', related_name='zp11'),
        ),
        migrations.AddField(
            model_name='sklad',
            name='pozycja_2',
            field=models.ForeignKey(to='Mecze.Pozycja', default='', related_name='zp2'),
        ),
        migrations.AddField(
            model_name='sklad',
            name='pozycja_3',
            field=models.ForeignKey(to='Mecze.Pozycja', default='', related_name='zp3'),
        ),
        migrations.AddField(
            model_name='sklad',
            name='pozycja_4',
            field=models.ForeignKey(to='Mecze.Pozycja', default='', related_name='zp4'),
        ),
        migrations.AddField(
            model_name='sklad',
            name='pozycja_5',
            field=models.ForeignKey(to='Mecze.Pozycja', default='', related_name='zp5'),
        ),
        migrations.AddField(
            model_name='sklad',
            name='pozycja_6',
            field=models.ForeignKey(to='Mecze.Pozycja', default='', related_name='zp6'),
        ),
        migrations.AddField(
            model_name='sklad',
            name='pozycja_7',
            field=models.ForeignKey(to='Mecze.Pozycja', default='', related_name='zp7'),
        ),
        migrations.AddField(
            model_name='sklad',
            name='pozycja_8',
            field=models.ForeignKey(to='Mecze.Pozycja', default='', related_name='zp8'),
        ),
        migrations.AddField(
            model_name='sklad',
            name='pozycja_9',
            field=models.ForeignKey(to='Mecze.Pozycja', default='', related_name='zp9'),
        ),
        migrations.AddField(
            model_name='sklad',
            name='zawodnik_1',
            field=models.ForeignKey(to='Mecze.Zawodnik', default='', related_name='z1'),
        ),
        migrations.AddField(
            model_name='sklad',
            name='zawodnik_10',
            field=models.ForeignKey(to='Mecze.Zawodnik', default='', related_name='z10'),
        ),
        migrations.AddField(
            model_name='sklad',
            name='zawodnik_11',
            field=models.ForeignKey(to='Mecze.Zawodnik', default='', related_name='z11'),
        ),
        migrations.AddField(
            model_name='sklad',
            name='zawodnik_2',
            field=models.ForeignKey(to='Mecze.Zawodnik', default='', related_name='z2'),
        ),
        migrations.AddField(
            model_name='sklad',
            name='zawodnik_3',
            field=models.ForeignKey(to='Mecze.Zawodnik', default='', related_name='z3'),
        ),
        migrations.AddField(
            model_name='sklad',
            name='zawodnik_4',
            field=models.ForeignKey(to='Mecze.Zawodnik', default='', related_name='z4'),
        ),
        migrations.AddField(
            model_name='sklad',
            name='zawodnik_5',
            field=models.ForeignKey(to='Mecze.Zawodnik', default='', related_name='z5'),
        ),
        migrations.AddField(
            model_name='sklad',
            name='zawodnik_6',
            field=models.ForeignKey(to='Mecze.Zawodnik', default='', related_name='z6'),
        ),
        migrations.AddField(
            model_name='sklad',
            name='zawodnik_7',
            field=models.ForeignKey(to='Mecze.Zawodnik', default='', related_name='z7'),
        ),
        migrations.AddField(
            model_name='sklad',
            name='zawodnik_8',
            field=models.ForeignKey(to='Mecze.Zawodnik', default='', related_name='z8'),
        ),
        migrations.AddField(
            model_name='sklad',
            name='zawodnik_9',
            field=models.ForeignKey(to='Mecze.Zawodnik', default='', related_name='z9'),
        ),
    ]
