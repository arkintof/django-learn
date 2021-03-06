# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uProfile', '0009_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='commentId',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='quesId',
            new_name='ques',
        ),
        migrations.RenameField(
            model_name='replies',
            old_name='replyId',
            new_name='reply',
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(upload_to='uProfile/media/'),
        ),
    ]
