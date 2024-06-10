from django.db import models

#SCIS User
class user(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    email = models.CharField(max_length=200)
    username = models.CharField(max_length=25)

#User's country of origin
class location(models.Model):
    country_origin = models.CharField(max_length=20) #Malaysia, Indonesia, etc...

#Medicine record
class record(models.Model):
    record_name = models.CharField(max_length=50)
    