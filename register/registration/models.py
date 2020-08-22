from django.db import models

# Create your models here.
class Person_data(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.TextField(max_length=100)
    confirm_password = models.TextField(max_length=100)