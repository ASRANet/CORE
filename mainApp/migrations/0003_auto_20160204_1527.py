# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-04 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_auto_20160204_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infopage',
            name='template',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]