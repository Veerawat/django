from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=300)
    nick_name = models.CharField(max_length=300, default="")
    email = models.CharField(max_length=100, default="")
    tel = models.CharField(max_length=10, default="")


class Subscriber(models.Model):
    email = models.CharField(max_length=100, default="")
