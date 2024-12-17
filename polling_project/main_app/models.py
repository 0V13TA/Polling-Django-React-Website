from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    profile_picture = models.ImageField()


class PollData(models.Model):
    title = models.TextField()
