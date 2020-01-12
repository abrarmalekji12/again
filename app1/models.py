from django.db import models

# Create your models here.
class MuOff(models.Model):
    email=models.CharField(max_length=50,primary_key=True)
    passw=models.CharField(max_length=50)
class InsOff(models.Model):
    email=models.CharField(max_length=50,primary_key=True)
    passw=models.CharField(max_length=50)
