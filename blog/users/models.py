from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.

class Register(models.Model):
    login = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    website = models.CharField(max_length=200)
    isadmin = models.CharField(max_length=1)

    def signUp(self):
        self.signUp_date = timezone.now()
        self.save()

    def __str__(self):
        return self.firstname