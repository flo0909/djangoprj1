from django.db import models
from feature.models import Ticket
from django.contrib.auth.models import User


class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    added = models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.cart_id) 


class CartItem(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    def total(self):
        return ticket.price * self.quantity
    def __str__(self):
        return str(self.ticket)


class Order(models.Model):
    order_number = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    added = models.DateField(auto_now_add=True)
    user_is_vip = models.BooleanField(default=True)
    off = models.DecimalField(max_digits=10, decimal_places=2, default=0.10)
    email = models.CharField(max_length=250)
    billingName = models.CharField(max_length=250)
    billingAddress1 = models.CharField(max_length=250)
    billingcity = models.CharField(max_length=250)
    billingPostcode = models.CharField(max_length=250)
    billingCountry = models.CharField(max_length=250)
    shippingName = models.CharField(max_length=250)
    shippingAddress1 = models.CharField(max_length=250)
    shippingcity = models.CharField(max_length=250)
    shippingPostcode = models.CharField(max_length=250)
    shippingCountry = models.CharField(max_length=250)
    def __str__(self):
        return str(self.order_number)
        
    
