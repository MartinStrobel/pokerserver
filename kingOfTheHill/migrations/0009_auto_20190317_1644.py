# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-17 08:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kingOfTheHill', '0008_auto_20190316_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournamentfight',
            name='player1_pot',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='tournamentfight',
            name='player2_pot',
            field=models.IntegerField(default=-1),
        ),
    ]
