from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.viewHomepage, name='home'),
    path('signup/', views.viewsignuppage, name='signup'),
    path('logout/', views.logoutUser, name='logout'),

]