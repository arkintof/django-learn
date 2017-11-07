# -*- coding: utf-8 -*-

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from django.db import models


class Userprofile(models.Model):
    ufname = models.CharField(db_column='uFName', max_length=100)  # Field name made lowercase.
    ulname = models.CharField(db_column='uLName', max_length=100)  # Field name made lowercase.
    id = models.AutoField(db_column='uId', primary_key=True)  # Field name made lowercase.
    udob = models.DateField(db_column='uDOB')  # Field name made lowercase.
    uemailid = models.CharField(db_column='uEmailId', max_length=250, blank=True,
                                null=True)  # Field name made lowercase.
    uimg = models.ImageField(db_column='uImg', max_length=1000)
    uAgeLimit = models.BooleanField(db_column='AgeLimit', default=False)


    def __str__(self):
        return self.ufname

    class Meta:
        managed = True
        db_table = 'UserProfile'

class Profile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(upload_to="uProfile/media/")

class QandA(models.Model):
    id = models.AutoField(primary_key=True)
    heading = models.CharField(db_column='qHead', max_length=120)
    question = models.TextField(db_column='question')
    img = models.CharField(db_column='qImg', max_length=200)
    type = models.CharField(db_column='qtype', max_length=100)
    checked = models.BooleanField(default=False)


    def __str__(self):
        return self.question

    class Meta:
        managed = True
        db_table = 'QandA'

class options(models.Model):
    qId = models.ForeignKey(QandA,on_delete=models.CASCADE)
    option = models.CharField(db_column='option',max_length=200)

    def __str__(self):
        return self.option


    class Meta:
        managed = True
        db_table = 'options'

class answer(models.Model):
    aId = models.ForeignKey(QandA,on_delete=models.CASCADE)
    answer = models.ForeignKey(options,on_delete=models.CASCADE)

    def __str__(self):
        return self.answer

    class Meta:
        managed = True
        db_table = 'answer'



class Comments(models.Model):
    Id = models.ForeignKey(User,on_delete=models.CASCADE)
    ques = models.ForeignKey(QandA,on_delete=models.CASCADE)
    comment = models.AutoField(primary_key=True)
    Text = models.TextField()
    date = models.DateTimeField(auto_now=True)

class Replies(models.Model):
    reply = models.ForeignKey(User,on_delete=models.CASCADE)
    Text = models.TextField()
    commentId = models.ForeignKey(Comments,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

