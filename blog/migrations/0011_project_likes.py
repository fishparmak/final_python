# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-11-11 03:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_organization_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='likes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]