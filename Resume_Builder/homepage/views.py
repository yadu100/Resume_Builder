from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def viewHomepage(request):
    return render(request, 'homepage/homepage.html',{})


def viewsignuppage(request):

    form = UserCreationForm()
    if request.method == 'POST':
        print(request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
            
    return render(request, 'homepage/signup.html', {'form':form})

def logoutUser(request):
    logout(request)
    return redirect('home')