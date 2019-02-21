from django.contrib import admin
from django.urls import path
#import Blogapp.views   <- 같은뜻
from .import views

urlpatterns =[
    path('<int:blog_id>', views.detail, name="detail"),
    path('create/', views.create, name="create"),
    path('write/',views.write, name="write"),
    path('ad',views.ad, name="ad"),
    path('rewrite/<int:blog_id>', views.rewrite, name="rewrite"),
    path('recreate/<int:blog_id>', views.recreate, name="recreate"),
    path('delete/<int:blog_id>', views.delete, name="delete"),
] 