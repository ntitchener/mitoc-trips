# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-02 06:34
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ws', '0012_new_prices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.PositiveIntegerField(validators=[
                django.core.validators.MaxValueValidator(2021),
                django.core.validators.MinValueValidator(1903)
            ]),
        ),
    ]