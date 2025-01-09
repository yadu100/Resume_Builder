from django.shortcuts import render

# Create your views here.
def HomepageCall(request):
    return render(request, 'Homepage/Homepage.html', {})

def LoginPageCall(request):
    return render(request, 'Homepage/login.html', {})
