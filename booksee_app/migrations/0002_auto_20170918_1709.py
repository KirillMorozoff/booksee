# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-18 14:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booksee_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Topic',
            new_name='Genre',
        ),
    ]