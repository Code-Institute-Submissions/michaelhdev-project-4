# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-25 18:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderlineitem',
            old_name='quantity',
            new_name='donation',
        ),
    ]
