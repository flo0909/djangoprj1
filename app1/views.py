from django.shortcuts import render, redirect, reverse
from .models import UserPost, Answer
from .forms import PostForm, AnswerForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.contrib import auth , messages
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    return render(request, 'app1/index.html')


@login_required
def postslist(request):


    profile = UserProfile.objects.all()
    
    posts_obj = UserPost.objects.order_by('-date_posted')
    paginator = Paginator(posts_obj, 3)
    page = request.GET.get('page')
    userpost = paginator.get_page(page)
    form = PostForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        form = PostForm()
    return render(request, 'app1/postslist.html', {'userpost':userpost, 'form':form, 'profile':profile })


@login_required
def postdetail(request, userpost_id):
    
    
    answer = 'There is no answer yet'
    userpost = get_object_or_404(UserPost, pk=userpost_id)
    try:
        profile = get_object_or_404(UserProfile, user=userpost.author)
        
    except ObjectDoesNotExist:
        pass
    try:
        answer = Answer.objects.get(name=userpost.name)
    except ObjectDoesNotExist:
        pass
    return render(request, 'app1/postdetail.html', {'userpost':userpost, 'answer':answer , 'profile':profile})

@login_required
def deleteuserpost(request, userpost_id):
    form = UserPost.objects.filter(pk=userpost_id)
    
    if request.method == 'POST':
        form.delete()
    return redirect(reverse('app1:postslist'))

@login_required
def updateuserpost(request, userpost_id):
 
    userpost = UserPost.objects.get(pk=userpost_id)
    if request.POST:
        form = PostForm(request.POST)
    if form.is_valid():
        userpost = UserPost.objects.get(pk=userpost_id)
        form = PostForm(request.POST, instance = userpost)
        form.save()
        return redirect(reverse('app1:postslist')) 
    else:      
        u_form = {"name": userpost.name, "content":userpost.content} 
        form = PostForm(initial=u_form)
        
    return render(request, 'app1/postupdate.html',{'form':form})

@login_required
def postresult(request, userpost_id):
    mylist = ''
    userpost = get_object_or_404(UserPost, pk=userpost_id)
    if request.method == 'POST':
        User.objects.filter(username=request.user)
        value = int(request.POST['value']) 
        userpost.votes += value

        if request.user.username in userpost.voted:
            messages.warning(request, "You already voted for this post!")
            return redirect(reverse('app1:postslist'))

        elif not request.user.username in userpost.voted:        
            mylist = ' ' + str(request.user.username) + ' ' 
            savedVoted = userpost.voted
            userpost.voted  = mylist + savedVoted
            userpost.save()

    return redirect(reverse('app1:postdetail', args=(userpost.id,)))

def answer(request, userpost_id):
    answer = []
    form = AnswerForm(request.POST)
    userpost = get_object_or_404(UserPost, pk=userpost_id)
    try:
        answer = Answer.objects.get(name=userpost.name)
    except ObjectDoesNotExist:
        form = AnswerForm(request.POST)
        if request.method == 'POST':
            answer = Answer.objects.create(name=userpost.name, content=request.POST['content'])
            return redirect(reverse('app1:postslist'))
    return render(request, 'app1/postanswer.html', {'form':form, 'answer':answer, 'userpost':userpost})
