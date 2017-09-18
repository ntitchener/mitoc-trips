# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-09-18 00:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ws', '0001_initial_squashed_migration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaderrating',
            name='activity',
            field=models.CharField(choices=[('biking', 'Biking'), ('boating', 'Boating'), ('cabin', 'Cabin'), ('climbing', 'Climbing'), ('hiking', 'Hiking'), ('winter_school', 'Winter School'), ('circus', 'Circus'), ('official_event', 'Official Event'), ('course', 'Course')], max_length=31),
        ),
        migrations.AlterField(
            model_name='leaderrecommendation',
            name='activity',
            field=models.CharField(choices=[('biking', 'Biking'), ('boating', 'Boating'), ('cabin', 'Cabin'), ('climbing', 'Climbing'), ('hiking', 'Hiking'), ('winter_school', 'Winter School'), ('circus', 'Circus'), ('official_event', 'Official Event'), ('course', 'Course')], max_length=31),
        ),
        migrations.AlterField(
            model_name='trip',
            name='activity',
            field=models.CharField(choices=[('biking', 'Biking'), ('boating', 'Boating'), ('cabin', 'Cabin'), ('climbing', 'Climbing'), ('hiking', 'Hiking'), ('winter_school', 'Winter School'), ('circus', 'Circus'), ('official_event', 'Official Event'), ('course', 'Course')], default='winter_school', max_length=31),
        ),
        migrations.AlterField(
            model_name='trip',
            name='algorithm',
            field=models.CharField(choices=[('lottery', 'lottery'), ('fcfs', 'first-come, first-serve')], default='lottery', max_length=31),
        ),
        migrations.AlterField(
            model_name='trip',
            name='lottery_task_id',
            field=models.CharField(blank=True, max_length=36, null=True, unique=True),
        ),
    ]