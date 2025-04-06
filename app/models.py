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
    login_id=models.ForeignKey(Login,on_delete=models.CASCADE)
    
class Advertisement(models.Model):
    media=models.FileField(upload_to='uploads/')
    station_id=models.ForeignKey(Station,on_delete=models.CASCADE,null=True,blank=True)

class slotbooking(models.Model):
    login_id = models.ForeignKey(Login, related_name='station_login', on_delete=models.CASCADE)  
    user_id = models.ForeignKey(Login, related_name='user_login', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    current_date = models.DateField(auto_now_add=True)
    cancel_status=models.IntegerField(default=0)
    
class feedback(models.Model):
    login_id = models.ForeignKey(Login,on_delete=models.CASCADE)
    feedback = models.TextField(blank=True,null=True)  
    station_id = models.ForeignKey(Station,on_delete=models.CASCADE)
    current_date = models.DateField(auto_now_add=True)

class complaints(models.Model):
    user_logid = models.ForeignKey(Login, on_delete=models.CASCADE)
    complaint=models.TextField(max_length=100)
    current_date=models.DateField(auto_now_add=True)
    reply=models.CharField(max_length=106,null=True)

class payment(models.Model):
    cardownername=models.CharField(max_length=25)
    cardno = models.CharField(max_length=15)
    cvv = models.CharField(max_length=5)
    expmonth_year = models.IntegerField()
    amount = models.IntegerField(default=0)
    bookingid = models.ForeignKey(slotbooking,on_delete=models.CASCADE,null=True,blank=True)
    login_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    current_date = models.DateTimeField(auto_now_add=True)
   

    
    


   


    