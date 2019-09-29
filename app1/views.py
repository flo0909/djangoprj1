from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'app1/index.html')
def postslist(request):
    return render(request, 'app1/postslist.html')
def postdetail(request):
    return render(request, 'app1/postdetail.html')