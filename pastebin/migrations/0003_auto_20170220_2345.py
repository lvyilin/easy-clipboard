# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pastebin', '0002_auto_20170220_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clipboard',
            name='create_date',
            field=models.DateTimeField(verbose_name='create date'),
        ),
    ]
