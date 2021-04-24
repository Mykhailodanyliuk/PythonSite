from django.shortcuts import render
from .models import Products
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


def mainpage(request):
    products = Products.objects.all()
    names=['dfgh','dfgh','dfcgvhb','ghj']
    return render(request,'mainpage/mainpage.html',{'first':products})

def registration(request):
    form = UserCreationForm()
    return render(request,'mainpage/registration.html',{'form':form})


def login(request):
    return render(request,'mainpage/login.html')