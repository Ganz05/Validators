from django.db import models

# Create your models here.


class Animal(models.Model):
    name=models.CharField(max_length=100)
    zoo=models.CharField(max_length=100)
    aid=models.IntegerField()
    re_enter=models.IntegerField()

