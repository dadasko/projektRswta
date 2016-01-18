# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mecze', '0029_auto_20151221_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sklad',
            name='nazwa_skladu',
            field=models.CharField(blank=True, max_length=16),
        ),
        migrations.AlterField(
            model_name='sklad',
            name='pozycja_1',
            field=models.ForeignKey(null=True, related_name='zp1', to='Mecze.Pozycja', default=''),
        ),
        migrations.AlterField(
            model_name='sklad',
            name='pozycja_10',
            field=models.ForeignKey(null=True, related_name='zp10', to='Mecze.Pozycja', default=''),
        ),
        migrations.AlterField(
            model_name='sklad',
            name='pozycja_11',
            field=models.ForeignKey(null=True, related_name='zp11', to='Mecze.Pozycja', default=''),
        ),
        migrations.AlterField(
            model_name='sklad',
            name='pozycja_2',
            field=models.ForeignKey(null=True, related_name='zp2', to='Mecze.Pozycja', default=''),
        ),
        migrations.AlterField(
            model_name='sklad',
            name='pozycja_3',
            field=models.ForeignKey(null=True, related_name='zp3', to='Mecze.Pozycja', default=''),
        ),
        migrations.AlterField(
            model_name='sklad',
            name='pozycja_4',
            field=models.ForeignKey(null=True, related_name='zp4', to='Mecze.Pozycja', default=''),
        ),
        migrations.AlterField(
            model_name='sklad',
            name='pozycja_5',
            field=models.ForeignKey(null=True, related_name='zp5', to='Mecze.Pozycja', default=''),
        ),
        migrations.AlterField(
            model_name='sklad',
            name='pozycja_6',
            field=models.ForeignKey(null=True, related_name='zp6', to='Mecze.Pozycja', default=''),
        ),
        migrations.AlterField(
            model_name='sklad',
            name='pozycja_7',
            field=models.ForeignKey(null=True, related_name='zp7', to='Mecze.Pozycja', default=''),
        ),
        migrations.AlterField(
            model_name='sklad',
            name='pozycja_8',
            field=models.ForeignKey(null=True, related_name='zp8', to='Mecze.Pozycja', default=''),
        ),
        migrations.AlterField(
            model_name='sklad',
            name='pozycja_9',
            field=models.ForeignKey(null=True, related_name='zp9', to='Mecze.Pozycja', default=''),
        ),
        migrations.AlterField(
            model_name='sklad',
            name='zawodnik_1',
            field=models.ForeignKey(null=True, related_name='z1', to='Mecze.Zawodnik', default=''),
        ),
        migrations.AlterField(
            model_name='sklad',
            name='zawodnik_10',
            field=models.ForeignKey(null=True, related_name='z10', to='Mecze.Zawodnik', default=''),
        ),
        migrations.AlterField(
            model_name='sklad',
            name='zawodnik_11',
            field=models.ForeignKey(null=True, related_name='z11', to='Mecze.Zawodnik', default=''),
        ),
        migrations.AlterField(
            model_name='sklad',
            name='zawodnik_2',
            field=models.ForeignKey(null=True, related_name='z2', to='Mecze.Zawodnik', default=''),
        ),
        migrations.AlterField(
            model_name='sklad',
            name='zawodnik_3',
            field=models.ForeignKey(null=True, related_name='z3', to='Mecze.Zawodnik', default=''),
        ),
        migrations.AlterField(
            model_name='sklad',
            name='zawodnik_4',
            field=models.ForeignKey(null=True, related_name='z4', to='Mecze.Zawodnik', default=''),
        ),
        migrations.AlterField(
            model_name='sklad',
            name='zawodnik_5',
            field=models.ForeignKey(null=True, related_name='z5', to='Mecze.Zawodnik', default=''),
        ),
        migrations.AlterField(
            model_name='sklad',
            name='zawodnik_6',
            field=models.ForeignKey(null=True, related_name='z6', to='Mecze.Zawodnik', default=''),
        ),
        migrations.AlterField(
            model_name='sklad',
            name='zawodnik_7',
            field=models.ForeignKey(null=True, related_name='z7', to='Mecze.Zawodnik', default=''),
        ),
        migrations.AlterField(
            model_name='sklad',
            name='zawodnik_8',
            field=models.ForeignKey(null=True, related_name='z8', to='Mecze.Zawodnik', default=''),
        ),
        migrations.AlterField(
            model_name='sklad',
            name='zawodnik_9',
            field=models.ForeignKey(null=True, related_name='z9', to='Mecze.Zawodnik', default=''),
        ),
    ]
