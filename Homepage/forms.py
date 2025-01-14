from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Headers
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
        fields = '__all__'

        widgets = {
            'user': forms.TextInput(attrs={'class':'form-control'}),
            'full_name': forms.TextInput(attrs={'class':'form-control'}),
            'applying_role': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control'}),

            

        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Disable 'user' and 'email' fields
        self.fields['user'].disabled = True
        self.fields['email'].disabled = True