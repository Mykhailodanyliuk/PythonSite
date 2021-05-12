from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Products
from django.http import HttpResponse
from .forms import ProductsForm
from .forms import UserRegisterForm,UserLoginForm
from django.contrib import messages
from django.contrib.auth import login,logout
from django.contrib.auth.mixins import LoginRequiredMixin

from .templatetags.auth_extras import has_group


def mainpage(request):
    products = Products.objects.all()
    names=['dfgh','dfgh','dfcgvhb','ghj']
    return render(request,'mainpage/mainpage.html',{'Products':products})

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
    if request.user.is_staff or has_group(request.user,'Sellers'):
        if request.method == 'POST':
            form = ProductsForm(data=request.POST)
            if form.is_valid():
                form.instance.author = request.user
                form.save()
                return redirect('mainpage')
        else:
            form = ProductsForm()
        data = {'form': form}
        return render(request,'mainpage/createproduct.html',data)
    else:
        return redirect('mainpage')

def updateproduct(request,pk):
    if request.user.is_staff:
        product = Products.objects.get(id=pk)
        form = ProductsForm(instance=product)
        if request.method == 'POST':
            form = ProductsForm(request.POST, instance=product)
            if form.is_valid():
                form.save()
                return redirect('/')

        context = {'form':form}
        return render(request,'mainpage/updateproduct.html',context)
    else:
        return redirect('registration')

def deleteproduct(request,pk):
    if request.user.is_staff:
        product = Products.objects.get(id=pk)
        if request.method == 'POST':
            product.delete()
            return redirect('/')
        context = {'item': product}
        return render(request, 'mainpage/deleteproduct.html', context)
    else:
        return redirect('registration')

