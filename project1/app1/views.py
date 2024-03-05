from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    Rform = RegisterForm(request.POST)
    dict={'Regform':Rform}
    if request.method == "POST":
        if Rform.is_valid():
            user=Rform.save()
            user.set_password(user.password)
            user.save()
            messages.success(request,"Registration successful..")
            return redirect('login')
        else:
            messages.error(request,'Invalid form submission..')
    return render(request,'Register.html',dict)