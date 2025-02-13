from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=50)
    contact=models.CharField(max_length=15)
    login_id=models.ForeignKey('Login',on_delete=models.CASCADE)

class Login(models.Model):
    email=models.EmailField(unique=True, null=True)
    password=models.CharField(max_length=30)
    usertype=models.CharField(max_length=20,null=True)

class Station(models.Model):
    state=models.CharField(max_length=60)
    district=models.CharField(max_length=60)
    city=models.CharField(max_length=60)
    location=models.CharField(max_length=60)
    login_id=models.ForeignKey('Login',on_delete=models.CASCADE)
    
class Advertisement(models.Model):
    media=models.FileField(upload_to='uploads/')
    station_id=models.ForeignKey(Station,on_delete=models.CASCADE,null=True,blank=True)





   


    