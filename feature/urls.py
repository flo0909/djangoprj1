from django.urls import path
from . import views
app_name='feature'
urlpatterns = [
    path('ticketlist/', views.ticketlist, name='ticketlist'),
    path('ticketdetail/<int:ticket_id>/', views.ticketdetail, name='ticketdetail'),
    path('ticketresult/<int:ticket_id>/', views.ticketresult, name='ticketresult'),
    path('ticketdelete/<int:ticket_id>/', views.ticketdelete, name='ticketdelete'),
    path('ticketupdate/<int:ticket_id>/', views.ticketupdate, name='ticketupdate'),
    path('ticketanswer/<int:ticket_id>/', views.ticketanswer, name='ticketanswer'),
]