from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomepageCall, name='homepage'),
    path('login/', views.LoginUser, name='login'),
    path('logout/',views.LogoutUser, name='logout'),
    path('register/', views.RegisterUser, name='register'),
    path('header/', views.HeaderPage, name='header'),
]