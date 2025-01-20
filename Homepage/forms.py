from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Headers,ProfessionalExperience,Education,Languages,Skills,Hobbies
from django.forms import ModelForm

class CustomUserCreationFrom(UserCreationForm):

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}),   
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}),
    )
    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter username'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder': 'Enter email'}),
            'password1': forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Enter password'}),
            'password2': forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Confirm password'}),

            

        }

        help_texts = {
            'username':None,
            'password1':None,
            'password2':None
        }

class HeaderForm(ModelForm):
    class Meta:
        model = Headers
        fields = ['full_name','applying_role','email','phone','location','basic_intro']

        widgets = {
            'full_name': forms.TextInput(attrs={'class':'form-control'}),
            'applying_role': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control'}),
            'basic_intro':  forms.Textarea(attrs={'class':'form-control','rows':10}),
            

            

        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Disable 'user' and 'email' fields
        self.fields['email'].disabled = True

class ProfessionalExperienceForm(ModelForm):
    class Meta:
        model = ProfessionalExperience
        fields = ['company1','location1','start_date1','designation1','job_description1','company2','location2','start_date2','end_date2','designation2','job_description2','company3','location3','start_date3','end_date3','designation3','job_description3','company4','location4','start_date4','end_date4','designation4','job_description4',]

        widgets = {
            'company1': forms.TextInput(attrs={'class':'form-control'}),
            'location1': forms.TextInput(attrs={'class':'form-control'}),
            'start_date1': forms.DateInput(attrs={'class':'form-control'}),
            'designation1':forms.TextInput(attrs={'class':'form-control'}),
            'job_description1': forms.Textarea(attrs={'class':'form-control','rows':10}),

            'company2': forms.TextInput(attrs={'class':'form-control'}),
            'location2': forms.TextInput(attrs={'class':'form-control'}),
            'start_date2': forms.DateInput(attrs={'class':'form-control'}),
            'end_date2': forms.DateInput(attrs={'class':'form-control'}),
            'designation2':forms.TextInput(attrs={'class':'form-control'}),
            'job_description2': forms.Textarea(attrs={'class':'form-control','rows':10}),

            'company3': forms.TextInput(attrs={'class':'form-control'}),
            'location3': forms.TextInput(attrs={'class':'form-control'}),
            'start_date3': forms.DateInput(attrs={'class':'form-control'}),
            'end_date3': forms.DateInput(attrs={'class':'form-control'}),
            'designation3':forms.TextInput(attrs={'class':'form-control'}),
            'job_description3': forms.Textarea(attrs={'class':'form-control','rows':10}),

            'company4': forms.TextInput(attrs={'class':'form-control'}),
            'location4': forms.TextInput(attrs={'class':'form-control'}),
            'start_date4': forms.DateInput(attrs={'class':'form-control'}),
            'end_date4': forms.DateInput(attrs={'class':'form-control'}),
            'designation4':forms.TextInput(attrs={'class':'form-control'}),
            'job_description4': forms.Textarea(attrs={'class':'form-control','rows':10}),
        }

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = ['degree1','school1','locationed1','cgpa1','started_date1','ended_date1','degree2','school2','locationed2','cgpa2','started_date2','ended_date2','degree3','school3','locationed3','cgpa3','started_date3','ended_date3']

        widgets = {
            'degree1':forms.TextInput(attrs={'class':'form-control'}),
            'school1':forms.TextInput(attrs={'class':'form-control'}),
            'locationed1':forms.TextInput(attrs={'class':'form-control'}),
            'cgpa1': forms.NumberInput(attrs={'class':'form-control','step':'0.01','min':'0','max':'10'}),
            'started_date1': forms.DateInput(attrs={'class':'form-control'}),
            'ended_date1': forms.DateInput(attrs={'class':'form-control'}),

            'degree2':forms.TextInput(attrs={'class':'form-control'}),
            'school2':forms.TextInput(attrs={'class':'form-control'}),
            'locationed2':forms.TextInput(attrs={'class':'form-control'}),
            'cgpa2': forms.NumberInput(attrs={'class':'form-control','step':'0.01','min':'0','max':'10'}),
            'started_date2': forms.DateInput(attrs={'class':'form-control'}),
            'ended_date2': forms.DateInput(attrs={'class':'form-control'}),

            'degree3':forms.TextInput(attrs={'class':'form-control'}),
            'school3':forms.TextInput(attrs={'class':'form-control'}),
            'locationed3':forms.TextInput(attrs={'class':'form-control'}),
            'cgpa3': forms.NumberInput(attrs={'class':'form-control','step':'0.01','min':'0','max':'10'}),
            'started_date3': forms.DateInput(attrs={'class':'form-control'}),
            'ended_date3': forms.DateInput(attrs={'class':'form-control'}),
        }

class LanguagesForm(ModelForm):
    class Meta:
        model = Languages
        fields = ['languages']

        widgets = {
            'languages': forms.Textarea(attrs={'class':'form-control','rows':10}),

        }

class SkillsForm(ModelForm):
    class Meta:
        model = Skills
        fields = ['skills']
        widgets = {
            'skills': forms.Textarea(attrs={'class':'form-control','rows':10}),

        }

class HobbiesForm(ModelForm):
    class Meta:
        model = Hobbies
        fields = ['hobbies']
        widgets = {
            'hobbies': forms.Textarea(attrs={'class':'form-control','rows':10}),

        }