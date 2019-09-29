from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput )


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Password' ,widget=forms.PasswordInput )
    password2 = forms.CharField(label='Confirm Password' ,widget=forms.PasswordInput )
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']