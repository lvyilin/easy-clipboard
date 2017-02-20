# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 15:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pastebin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clipboard',
            name='user',
        ),
        migrations.AddField(
            model_name='clipboard',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clipboard',
            name='paste_text',
            field=models.CharField(max_length=3000),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
