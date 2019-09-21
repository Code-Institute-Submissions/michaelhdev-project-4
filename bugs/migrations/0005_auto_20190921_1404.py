# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-21 14:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bugs', '0004_auto_20190920_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bug',
            name='votes',
        ),
        migrations.AddField(
            model_name='bug',
            name='votes',
            field=models.ManyToManyField(blank=True, related_name='votes', to=settings.AUTH_USER_MODEL),
        ),
    ]
