
from app.models import *
from django import forms
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm



class SignupForm(UserCreationForm):
    name=forms.CharField(label=("Full Name"))
    username = forms.EmailField(label=("Email"))


    class Meta:
        model=User
        fields=('name','username','password1','password2')




class TimeTableForm(forms.ModelForm):

    class Meta:
        model = Timetable
        fields = '__all__'