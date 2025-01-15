from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomepageCall, name='homepage'),
    path('login/', views.LoginUser, name='login'),
    path('logout/',views.LogoutUser, name='logout'),
    path('register/', views.RegisterUser, name='register'),
    path('header/', views.HeaderPage, name='header'),
    path('experience/',views.ProfessionalExperiencePage, name='experience'),
    path('education/',views.EducationPage,name='education'),
    path('other/',views.OtherDetailsPage, name='other')
]