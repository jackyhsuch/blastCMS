# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-22 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='contact',
            field=models.IntegerField(),
        ),
    ]