# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-21 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prokat', '0003_auto_20180519_1256'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]