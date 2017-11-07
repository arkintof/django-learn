# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Userprofile,QandA,Comments,Replies,Profile
# Register your models here.
class user(admin.ModelAdmin):
    list_display = ('id','ufname')
class QA(admin.ModelAdmin):
    list_display = ('id','heading')
admin.site.register(Userprofile,user)
admin.site.register(QandA,QA)
admin.site.register(Comments)
admin.site.register(Replies)
admin.site.register(Profile)

