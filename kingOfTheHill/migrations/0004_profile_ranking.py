# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-14 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kingOfTheHill', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ranking',
            field=models.IntegerField(null=True),
        ),
    ]
