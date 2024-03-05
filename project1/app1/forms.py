from django import forms
from django.contrib.auth.models import User
from .import models

class RegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password','first_name','last_name',]
        widgets={
            'password':forms.PasswordInput(),
            'first_name':forms.TextInput(),
            'email':forms.EmailInput()
        }