# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-08-23 13:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0005_auto_20200823_2104'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='book',
            table='mybook',
        ),
    ]
