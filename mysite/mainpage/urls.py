from django.urls import path

from . import views

urlpatterns = [
    path('', views.mainpage, name='index'),
    path('registration/', views.registration,name='registration'),
    path('login/',views.login,name='login')
]