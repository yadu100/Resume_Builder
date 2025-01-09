from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomepageCall, name='homepage'),
    path('login/', views.LoginPageCall, name='login'),
]