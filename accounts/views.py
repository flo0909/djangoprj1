from django.shortcuts import render, reverse, redirect
from django.contrib import auth, messages
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.core.exceptions import ObjectDoesNotExist
from .models import UserProfile

# code for login and register views with many thanks from Mr Brad Traversy's tutorial. 
# https://www.udemy.com/course/python-django-dev-to-deployment/



def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect(reverse('app1:index'))
        else:
            messages.warning(request, 'Incorrect username or password')
    else:    
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form':form})

@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are now logged out!')
    return redirect(reverse('app1:index'))

def register(request):
    
    form = UserRegisterForm(request.POST)
   

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 ==  password2:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'This username is already in use')
                return redirect(reverse('accounts:register'))
            else:
                if User.objects.filter(email=email).exists():
                    messages.warning(request, 'This email is already in use')
                    return redirect(reverse('accounts:register'))
                else:
                    if form.is_valid:
                        user = User.objects.create_user(username=username ,email=email, password=password1)
                        profile = UserProfile.objects.create(user=user, image='user_images/default.png')
                        messages.success(request, 'You have registered successfully')
                        return redirect(reverse('accounts:login'))
        else:
            messages.warning(request, 'The passwords do not match')
            return redirect(reverse('accounts:register'))

    else:
        form = UserRegisterForm() 
        
    return render(request, 'accounts/register.html', {"form": form})

# code for userprofile view with many thanks from Mr CoreyMSchafer's tutorial, changed to match with my app
# https://www.youtube.com/watch?v=CQ90L5jfldw&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=9

@login_required
def userprofile(request):
    if request.method == 'POST':
        userform = UserUpdateForm(request.POST, instance=request.user)
        userprofileform = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.userprofile)

        if userform and userprofileform.is_valid:
            userform.save()
            userprofileform.save()
            messages.success(request, 'You have successfully updated your profile')
            return redirect(reverse('app1:index'))

    else:
        userform = UserUpdateForm(instance=request.user)
        userprofileform = ProfileUpdateForm(instance=request.user.userprofile)


    return render(request, 'accounts/userprofile.html',dict(userform=userform, userprofileform=userprofileform) )