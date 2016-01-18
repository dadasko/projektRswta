# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bramka',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('minuta', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Kolejka',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('nr_kolejki', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mecz',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('uwagi', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Pozycja',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Sklad',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('id_pozycji', models.ForeignKey(to='Mecze.Pozycja')),
            ],
        ),
        migrations.CreateModel(
            name='Sklad_na_mecz',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('id_meczu', models.ForeignKey(to='Mecze.Mecz')),
                ('id_skladu', models.ForeignKey(to='Mecze.Sklad')),
            ],
        ),
        migrations.CreateModel(
            name='Wynik',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('gole_gospodarza', models.IntegerField()),
                ('gole_goscia', models.IntegerField()),
                ('id_kolejki', models.ForeignKey(to='Mecze.Kolejka')),
                ('id_meczu', models.ForeignKey(to='Mecze.Mecz')),
            ],
        ),
        migrations.CreateModel(
            name='Zawodnik',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('imie', models.CharField(max_length=50)),
                ('nazwisko', models.CharField(max_length=50)),
                ('id_pozycji', models.ForeignKey(to='Mecze.Pozycja')),
            ],
        ),
        migrations.CreateModel(
            name='Zespol',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='zawodnik',
            name='id_zespolu',
            field=models.ForeignKey(to='Mecze.Zespol'),
        ),
        migrations.AddField(
            model_name='sklad_na_mecz',
            name='id_zespolu',
            field=models.ForeignKey(to='Mecze.Zespol'),
        ),
        migrations.AddField(
            model_name='sklad',
            name='id_zawodnika',
            field=models.ForeignKey(to='Mecze.Zawodnik'),
        ),
        migrations.AddField(
            model_name='sklad',
            name='id_zespolu',
            field=models.ForeignKey(to='Mecze.Zespol'),
        ),
        migrations.AddField(
            model_name='mecz',
            name='id_goscia',
            field=models.ForeignKey(to='Mecze.Zespol', related_name='mecz_gosc'),
        ),
        migrations.AddField(
            model_name='mecz',
            name='id_gospodarza',
            field=models.ForeignKey(to='Mecze.Zespol', related_name='mecz_gospodarz'),
        ),
        migrations.AddField(
            model_name='mecz',
            name='id_kolejki',
            field=models.ForeignKey(to='Mecze.Kolejka'),
        ),
        migrations.AddField(
            model_name='mecz',
            name='id_wyniku',
            field=models.ForeignKey(to='Mecze.Wynik'),
        ),
        migrations.AddField(
            model_name='bramka',
            name='id_meczu',
            field=models.ForeignKey(to='Mecze.Mecz'),
        ),
        migrations.AddField(
            model_name='bramka',
            name='id_zawodnika',
            field=models.ForeignKey(to='Mecze.Zawodnik'),
        ),
    ]
