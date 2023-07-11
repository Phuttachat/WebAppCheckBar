from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
# Create your views here.

def Register(requsest):
    return render (requsest, 'myapp/register.html')

def Login(requsest):
    return render (requsest, 'myapp/login.html')

def Overview(requsest):
    return render (requsest, 'myapp/overview.html')

def BarThai(requsest):
    return render (requsest, 'myapp/barthai.html')

def EditBarThai(requsest):
    return render (requsest, 'myapp/editbarthai.html')

def NewBarThai(requsest):
    return render (requsest, 'myapp/newbarthai.html')

def BarEng(requsest):
    return render (requsest, 'myapp/bareng.html')

def EditBarEng(requsest):
    return render (requsest, 'myapp/editbareng.html')

def NewBarEng(requsest):
    return render (requsest, 'myapp/newbareng.html')

def Test(requsest):
    return render (requsest, 'myapp/test.html')