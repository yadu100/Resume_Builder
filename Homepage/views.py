from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationFrom, HeaderForm
from .models import Headers

# Create your views here.
def HomepageCall(request):
    return render(request, 'Homepage/Homepage.html', {})

def LoginUser(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    
    page = 'loginpage'

    if request.method == 'POST':
        # print(request.POST)
        user_mail = request.POST['Email']
        password = request.POST['Password']
        # print(user_mail,password)

        try:
            current_user = User.objects.get(email=user_mail)
        except:
            print('Invalid Email')
        
        user = authenticate(request, username = current_user.username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            print('Your User email and password doest not match')



    return render(request, 'Homepage/login.html', {'page':page})

def LogoutUser(request):
    logout(request)
    return redirect('homepage')


def RegisterUser(request):
    page="registerpage"
    form = CustomUserCreationFrom()
    if request.method == 'POST':
        form = CustomUserCreationFrom(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('header')
        else:
            print('There is a problem registering user. Please try again')
    return render(request,'Homepage/login.html',{'page':page, 'form':form})

def HeaderPage(request):
    current_user = request.user
    # print('current email')
    instance_email = current_user.email
    # print(instance_email)
    # print('all emails')
    # all_header_items = Headers.objects.all()
    # for header in all_header_items:
    #     print(header.email)
    header_item = Headers.objects.get(email=instance_email)
    form = HeaderForm(instance=header_item)
    if request.method == 'POST':
        form = HeaderForm(request.POST, instance=header_item)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(request,'Homepage/headerPage.html',{'form':form})


