from django.shortcuts import render, redirect, get_object_or_404, reverse
import os
from .models import CartItem, Cart, Order
from django.contrib import auth, messages
from django.core.exceptions import ObjectDoesNotExist
from feature.models import Ticket
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.conf import settings
import stripe


#cart app taken with many thanks from Mr Nestor Viloria's tutorial 
# https://www.udemy.com/course/develop-a-shopping-cart-website-with-django-2-and-python-3/
# parts of code changed by me to fit the purpose and make it functional in context

#creates a session that will be host the cart items
#uses the session key as the cart id
def cartId(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.get(request)
    return cart
# takes ticket objects, creates a cart using the session created by previous function
# assigns the cart items to cart
# saves the cart
def add(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    try:
        cart = Cart.objects.get(cart_id=cartId(request))
    except ObjectDoesNotExist:
        cart = Cart.objects.create( cart_id = cartId(request))
    try:
        cart_item = CartItem.objects.get(ticket=ticket, cart=cart)
        cart_item.quantity +=1
        cart_item.save()
    except ObjectDoesNotExist:
        cart_item = CartItem.objects.create(ticket=ticket, cart=cart, quantity=1)
    return redirect('cart:cart_detail')


# connects the cart items with stripe backend
# completes the purchase
# creates and saves the order, informations accessible in admin-order
# conditional if the order exists, user is VIP and gets a discount
def cart_detail(request, total=0, cart_items = None):
    try:
        cart = Cart.objects.get(cart_id=cartId(request))
        cart_items = CartItem.objects.filter(cart=cart).order_by('ticket')
        if Order is not None:
            order = Order.objects.filter(user=request.user).first()
         
        for cart_item in cart_items:
            if order is not None and order.user_is_vip == True:
    
                cart_item.ticket.price = cart_item.ticket.price - order.off
            else:
                cart_item.ticket.price = cart_item.ticket.price

            total += cart_item.ticket.price * cart_item.quantity 
    
    except ObjectDoesNotExist:
        pass

    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe_total = int(total * 100)
    description = 'New Order - Issue Tracker'
    data_key = settings.STRIPE_PUBLISHABLE_KEY

    if request.method == 'POST':

        try:
            token = request.POST['stripeToken']
            email = request.POST['stripeEmail']
            billingName = request.POST['stripeBillingName']
            billingAddress1 = request.POST['stripeBillingAddressLine1']
            billingcity = request.POST['stripeBillingAddressCity']
            billingPostcode = request.POST['stripeBillingAddressZip']
            billingCountry = request.POST['stripeBillingAddressCountryCode']
            shippingName = request.POST['stripeShippingName']
            shippingAddress1 = request.POST['stripeShippingAddressLine1']
            shippingcity = request.POST['stripeShippingAddressCity']
            shippingPostcode = request.POST['stripeShippingAddressZip']
            shippingCountry = request.POST['stripeShippingAddressCountryCode']
            customer = stripe.Customer.create(
                        email=email,
                        source = token
                )
            charge = stripe.Charge.create(
                        amount=stripe_total,
                        currency="gbp",
                        description=description,
                        customer=customer.id
                        )
            try:
                order=Order.objects.create(
                    order_number=token,
                    total=total,
                    user=request.user,
                    user_is_vip=True,
	                off = 0.10,
                    email = email,
                    billingName = billingName,
                    billingAddress1 = billingAddress1,
                    billingcity = billingcity,
                    billingPostcode = billingPostcode,
                    billingCountry = billingCountry,
                    shippingName = shippingName,
                    shippingAddress1 = shippingAddress1,
                    shippingcity = shippingcity,
                    shippingPostcode = shippingPostcode,
                    shippingCountry = shippingCountry,
                )
            except:
                pass
            cart_items.delete()
            cart.delete()
            return redirect('cart:order')
        except stripe.error.CardError as e:
            return False,e
    return render(request, 'cart/cart.html', dict(total=total, cart_items=cart_items, data_key = data_key, stripe_total = stripe_total, description = description))

# changes the quantity of cart items from cart
def remove(request, ticket_id):
    cart = Cart.objects.get(cart_id=cartId(request))
    ticket = get_object_or_404(Ticket, id=ticket_id)
    cart_item = CartItem.objects.get(ticket=ticket , cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    
    return redirect('cart:cart_detail')

def emptyCart(request):
	cart = Cart.objects.get(cart_id=cartId(request))
	cart.delete()
	return redirect('cart:cart_detail')

# redirects after purchase to an order page
def order(request):
    return render(request, 'cart/order.html')


