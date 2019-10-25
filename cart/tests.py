from django.test import TestCase
from .models import Cart, CartItem, Order

# Create your tests here.

class TestViews(TestCase):

    def test_get_cart_page(self):
        page = self.client.get("/cart/")
        self.assertTrue(page.status_code, 200)
        self.assertTemplateUsed(template_name='cart.html')
    
    def test_get_order_page(self):
        page = self.client.get("/order/")
        self.assertTrue(page.status_code, 200)
        self.assertTemplateUsed(template_name='order.html')

    
class TestModels(TestCase):

    def test_check_id(self):
        cart = Cart(cart_id="random_id")
        cart.save()
        self.assertEqual(cart.cart_id, "random_id")
        self.assertTrue(cart.cart_id, "random_id")

 
    

