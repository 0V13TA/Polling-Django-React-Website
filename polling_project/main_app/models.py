from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True, max_length=30)
    password = models.CharField(max_length=255)

class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)