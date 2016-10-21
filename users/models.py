from django.db import models


# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)
    matric_number = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.name
        
