from django.db import models

# Create your models here.


class profiles(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    mobile = models.CharField(max_length=15)
    college = models.CharField(max_length=100)
    course = models.CharField(max_length=25)
    messege = models.TextField(null=True)