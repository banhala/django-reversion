# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-11 00:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reversion', '0001_squashed_0003_auto_20160601_1600'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=191)),
                ('revision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reversion.Revision')),
            ],
        ),
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='v1', max_length=191)),
            ],
        ),
        migrations.CreateModel(
            name='TestModelParent',
            fields=[
                ('testmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='test_app.TestModel')),
                ('parent_name', models.CharField(default='v1', max_length=191)),
            ],
            bases=('test_app.testmodel',),
        ),
    ]