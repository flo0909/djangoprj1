from django.db import models
from feature.models import Ticket


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



    
