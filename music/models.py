from django.db import models

# Create your models here.

class Albums(models.Model):
	artist = models.CharField(max_length=250)
	
class User(models.Model):
	userName = models.CharField(primary_key = True,max_length = 250)
