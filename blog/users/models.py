from django.db import models
from django.conf import settings


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    website = models.CharField(max_length=200)
    isadmin = models.BooleanField(default=False)

    def __str__(self):
        return self.firstname + " " + self.lastname + " " + self.email + " " + self.website