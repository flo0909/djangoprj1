from django.shortcuts import render, reverse, redirect
from django.contrib import auth, messages
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegisterForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if form.is_valid():
            auth.login(request, user)
            messages.success(request, 'You have succesfully logged in')
            return redirect(reverse('app1:postslist'))
    else:    
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form':form})

@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are now logged out!')
    return redirect(reverse('app1:postslist'))

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        username = request.POST['username']
        email = request.POST['email'] 
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user = auth.authenticate(username=username, email=email, password1=password1, password2=password2)
        if form.is_valid():
            if User.objects.filter(email=email).exclude(username=username):
                messages.warning(request, 'This email is already being used' )
                return render(request, 'accounts/register.html', {'form':form} )
            else:
                if password1 == password2:
                    form.save()
                    messages.success(request, 'You are now registered and can login')
                    return redirect(reverse('accounts:login'))
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html',{'form':form})