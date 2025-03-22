from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=256)
    email=models.EmailField(max_length=100)

class product(models.Model):
    p_name=models.CharField(max_length=100)
    Quantity=models.IntegerField()
    price=models.IntegerField()

class Data(models.Model):
    Full_name=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100)
    Password=models.CharField(max_length=50)
    Usertype=models.CharField(max_length=50)