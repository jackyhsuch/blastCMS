from django.db import models

from users.models import Users


class Events(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    isCompulsory = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Attendances(models.Model):
    event = models.ForeignKey(Events)
    user = models.ForeignKey(Users)
    status = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
