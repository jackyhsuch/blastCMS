from django.db import models

from datetime import datetime


# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    contact = models.IntegerField()
    matric_number = models.CharField(max_length=200)
    batch_year = models.IntegerField(default=datetime.now().year)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

<<<<<<< HEAD
class Events(models.Model):
    name = models.CharField(max_length=200)
    date =  models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Attendances(models.Model):
    Event_id = models.CharField(max_length=200)
    User_id = models.CharField(max_length=200)
    Status = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  

=======
>>>>>>> 1dff2bd5ac8a4d82ccd3d750cbbe69580d069dba
    def __str__(self):
        sb = []

        for key in self.__dict__:
            sb.append("{key}='{value}'".format(key=key, value=self.__dict__[key]))

        return ', '.join(sb)
