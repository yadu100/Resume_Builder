from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationFrom, HeaderForm, ProfessionalExperienceForm,EducationForm,LanguagesForm,SkillsForm,HobbiesForm
from .models import Headers, ProfessionalExperience,Education,Languages,Skills,Hobbies
from django.contrib.auth.decorators import login_required

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

@login_required(login_url='login')
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
            return redirect('experience')
    return render(request,'Homepage/headerPage.html',{'form':form})


@login_required(login_url='login')
def ProfessionalExperiencePage(request):
    current_user = request.user
    current_user_name = current_user.username
    user_experience = ProfessionalExperience.objects.get(user=current_user_name)
    form = ProfessionalExperienceForm(instance=user_experience)
    if request.method == 'POST':
        form = ProfessionalExperienceForm(request.POST,instance=user_experience)
        if form.is_valid():
            form.save()
            return redirect('education')

    return render(request,'Homepage/professional_experience.html',{'form':form})


@login_required(login_url='login')
def EducationPage(request):
    current_user = request.user
    current_user_name = current_user.username
    user_education = Education.objects.get(user=current_user_name)
    form = EducationForm(instance=user_education)
    if request.method == 'POST':
        form = EducationForm(request.POST,instance=user_education)
        if form.is_valid():
            form.save()
            return redirect('other')

    return render(request,'Homepage/education.html',{'form':form})


@login_required(login_url='login')
def OtherDetailsPage(request):
    current_user = request.user
    current_user_name = current_user.username

    language_instance = Languages.objects.get(user = current_user_name)
    skills_instance = Skills.objects.get(user=current_user_name)
    hobbies_instance = Hobbies.objects.get(user=current_user_name)

    language_form = LanguagesForm(instance=language_instance)
    skills_form = SkillsForm(instance=skills_instance)
    hobbies_form = HobbiesForm(instance=hobbies_instance)

    if request.method == 'POST':

        language_form = LanguagesForm(request.POST,instance=language_instance)
        skills_form = SkillsForm(request.POST,instance=skills_instance)
        hobbies_form = HobbiesForm(request.POST,instance=hobbies_instance)

        if language_form.is_valid() and skills_form.is_valid() and hobbies_form.is_valid():
            language_form.save()
            skills_form.save()
            hobbies_form.save()

            return redirect('template')
        


    return render(request,'Homepage/other_details.html',{'language_form':language_form,'skills_form':skills_form,'hobbies_form':hobbies_form})