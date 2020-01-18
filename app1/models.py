from django.db import models

# Create your models here.
class MuOff(models.Model):
    email=models.CharField(max_length=50,primary_key=True)
    passw=models.CharField(max_length=50)

class InsOff(models.Model):
    email=models.CharField(max_length=50,primary_key=True)
    passw=models.CharField(max_length=50)

class Road(models.Model) :
    name=models.CharField(max_length=20)
    area=models.CharField(max_length=30)
    city=models.CharField(max_length=15)
    pin=models.IntegerField()
    length=models.FloatField()
    lane=models.IntegerField()
    
class Construction(models.Model) :
    road=models.ForeignKey(Road, on_delete=models.CASCADE) 
    inspector=models.ForeignKey(InsOff,on_delete=models.CASCADE)
    status=models.IntegerField()
    image=models.ImageField(upload_to="media/",null=True)
    fund=models.FloatField()
class Schedule(models.Model) : 
    start_date=models.DateField(auto_now=False, auto_now_add=False) 
    construction=models.ForeignKey(Construction, on_delete=models.CASCADE) 
    municipal=models.ForeignKey(MuOff,on_delete=models.CASCADE,null=True)   
class history(models.Model) :
     finish_date=models.DateField(auto_now=False, auto_now_add=False)  
     construction=models.ForeignKey(Construction, on_delete=models.CASCADE)
     municipal=models.ForeignKey(MuOff,on_delete=models.CASCADE,null=True)   