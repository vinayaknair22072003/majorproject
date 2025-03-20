from django import forms
from.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','contact']

class LoginCheck(forms.ModelForm):
    class Meta:
        model=Login
        fields=['email', 'password']


class LoginForm(forms.Form):
    email=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)
    

class Logineditform(forms.ModelForm):
    class Meta:
        model=Login
        fields=['email']

class StationForm(forms.ModelForm):
    class Meta:
        model=Station
        fields=['state','district','city','location']
    
class AdvertisementForm(forms.ModelForm):
    class Meta:
        model=Advertisement
        fields=['media']

class slotbook(forms.ModelForm):
    class Meta:
        model=slotbooking
        fields=['date','time']

class feedbackform(forms.ModelForm):
    class Meta:
        model=feedback
        fields=['feedback']

class complaintform(forms.ModelForm):
    class Meta:
        model=complaints
        fields=['complaint']



    

