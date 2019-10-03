from django.urls import path
from . import views

app_name='cart'
urlpatterns = [
	path('add/<int:ticket_id>/', views.add, name='add'),
	path('', views.cart_detail, name='cart_detail'),
	path('remove/<int:ticket_id>/', views.remove, name='remove'),
	path('emptyCart/', views.emptyCart, name='emptyCart'),
	path('order/', views.order, name='order'),
	
]