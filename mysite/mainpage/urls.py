from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('registration/', views.registration,name='registration'),
    path('user_login/',views.user_login,name='user_login'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('createproduct/',views.createproduct,name='createproduct'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico')))
]