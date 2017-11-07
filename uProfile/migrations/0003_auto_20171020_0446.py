# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 04:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uProfile', '0002_auto_20171020_0440'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='uid',
            new_name='id',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='uAgeLimit',
            field=models.BooleanField(db_column='AgeLimit', default=False),
        ),
    ]
