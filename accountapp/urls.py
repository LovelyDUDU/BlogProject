from django.contrib import admin
from django.urls import path
#import Blogapp.views   <- 같은뜻
from .import views

urlpatterns =[
    path('login/', views.login, name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/', views.logout,name='logout'),
] 