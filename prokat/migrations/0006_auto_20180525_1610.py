# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-25 13:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('prokat', '0005_auto_20180524_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='comment',
            field=models.CharField(default=django.utils.timezone.now, max_length=200, verbose_name='Ваш комментарий:'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='Желаемая дата'),
        ),
    ]