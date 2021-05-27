from django import forms
from django.db import models
from django.forms import fields
from .models import User
class Userform(forms.ModelForm):
    class Meta:
        model=User
        fields=('first_name','last_name','email','phone_no','password')