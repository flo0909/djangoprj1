from django.urls import path
from . import views
from feature.models import Ticket


app_name = 'progress'
urlpatterns = [
   path('progress/<int:ticket_id>/', views.progress, name='progress'), 
]