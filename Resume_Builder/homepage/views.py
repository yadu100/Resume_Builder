from django.shortcuts import render

# Create your views here.
def viewHomepage(request):
    return render(request, 'homepage/homepage.html',{})