# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-27 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksee_app', '0005_century'),
    ]

    operations = [
        migrations.CreateModel(
            name='Raiting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raiting_value', models.CharField(max_length=5, unique=True)),
            ],
        ),
    ]