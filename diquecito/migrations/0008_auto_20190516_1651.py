# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-05-16 16:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diquecito', '0007_auto_20190516_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='usuario_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
