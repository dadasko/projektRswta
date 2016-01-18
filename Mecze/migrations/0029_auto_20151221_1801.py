# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mecze', '0028_auto_20151219_1731'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bramka',
            old_name='id_meczu',
            new_name='mecz',
        ),
        migrations.RenameField(
            model_name='bramka',
            old_name='id_zawodnika',
            new_name='zawodnik',
        ),
        migrations.RenameField(
            model_name='mecz',
            old_name='id_goscia',
            new_name='gosc',
        ),
        migrations.RenameField(
            model_name='mecz',
            old_name='id_gospodarza',
            new_name='gospodarz',
        ),
        migrations.RenameField(
            model_name='mecz',
            old_name='id_kolejki',
            new_name='kolejka',
        ),
        migrations.RenameField(
            model_name='mecz',
            old_name='id_skladu_goscia',
            new_name='sklad_goscia',
        ),
        migrations.RenameField(
            model_name='mecz',
            old_name='id_skladu_gospodarza',
            new_name='sklad_gospodarza',
        ),
        migrations.RenameField(
            model_name='sklad',
            old_name='id_zespolu',
            new_name='zespol',
        ),
        migrations.RenameField(
            model_name='zawodnik',
            old_name='id_pozycji',
            new_name='pozycja',
        ),
        migrations.RenameField(
            model_name='zawodnik',
            old_name='id_zespolu',
            new_name='zespol',
        ),
    ]
