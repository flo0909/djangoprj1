from django.urls import path
from . import views
app_name='app1'
urlpatterns = [
    path('', views.index, name='index'),
    path('postslist/', views.postslist, name='postslist'),
    path('postdetail/<int:userpost_id>/', views.postdetail, name='postdetail'),
    path('postresult/<int:userpost_id>/', views.postresult, name='postresult'),
    path('deleteuserpost/<int:userpost_id>/', views.deleteuserpost, name='deleteuserpost'),
    path('updateuserpost/<int:userpost_id>/', views.updateuserpost, name='updateuserpost'),
]
