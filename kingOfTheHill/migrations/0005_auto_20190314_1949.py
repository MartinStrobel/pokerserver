# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-14 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kingOfTheHill', '0004_profile_ranking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='num_sub',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='ranking',
            field=models.IntegerField(default=-1, null=True),
        ),
    ]