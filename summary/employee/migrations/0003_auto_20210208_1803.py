# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-02-08 18:03
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employee', '0002_auto_20210208_1747'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalEmployee',
            fields=[
                ('employee_id', models.IntegerField(blank=True, db_index=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.CharField(db_index=True, max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical employee',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AlterField(
            model_name='department',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 8, 18, 3, 22, 423955)),
        ),
        migrations.AlterField(
            model_name='employee',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='historicalemployee',
            name='department',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='employee.Department'),
        ),
        migrations.AddField(
            model_name='historicalemployee',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
