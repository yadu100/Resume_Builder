from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

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