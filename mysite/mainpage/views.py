from django.shortcuts import render, redirect
from .models import Products
from django.http import HttpResponse
from .forms import ProductsForm
from .forms import UserRegisterForm,UserLoginForm
from django.contrib import messages
from django.contrib.auth import login,logout

def mainpage(request):
    products = Products.objects.all()
    names=['dfgh','dfgh','dfcgvhb','ghj']
    return render(request,'mainpage/mainpage.html',{'first':products})

def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,"Ви успішно зареєстровані")
            return redirect('mainpage')
        else:
            messages.error(request,'Помилка реєстрації')
    else:
        form = UserRegisterForm()
    return render(request,'mainpage/registration.html',{'form':form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.success(request, "Ви увійшли")
            return redirect('mainpage')
        else:
            messages.error(request, 'Помилка входу')
    else:
        form = UserLoginForm

    return render(request,'mainpage/login.html',{"form": form})

def user_logout(request):
    logout(request)
    return redirect('mainpage')

def createproduct(request):
    if request.method == 'POST':
        form = ProductsForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('mainpage')
    else:
        form = ProductsForm()
    data = {'form': form}
    return render(request,'mainpage/createproduct.html',data)