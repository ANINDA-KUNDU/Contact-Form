from django.db import models

# Create your models here.
class UserComments(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=200)
    comments = models.CharField(max_length=1000)