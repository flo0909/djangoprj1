from django.test import TestCase
from .forms import UserUpdateForm, UserCreationForm, UserLoginForm, UserRegisterForm
from .models import UserProfile

# Create your tests here.
class TestForms(TestCase):

    def test_login_with_username(self):
        form = UserLoginForm({'username': 'Myself'})
        self.assertFalse(form.is_valid())

    def test_no_input(self):
        form = UserLoginForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], ['This field is required.'])

    def test_register_with_username(self):
        form = UserRegisterForm({'username': 'Myself'})
        self.assertFalse(form.is_valid())

    def test_register_no_input(self):
        form = UserRegisterForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], ['This field is required.'])

    def test_update_with_email(self):
        form = UserUpdateForm({'email': 'example@example.com'})
        self.assertFalse(form.is_valid())

    def test_update_no_input(self):
        form = UserUpdateForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['This field is required.'])



class TestViews(TestCase):

    def test_get_login_page(self):
        page = self.client.get("/login/")
        self.assertTrue(page.status_code, 200)
        self.assertTemplateUsed(template_name='login.html')
        

    def test_get_register_page(self):
        page = self.client.get("/register/")
        self.assertTrue(page.status_code, 200)
        self.assertTemplateUsed(template_name='register.html')
        
    def test_get_userprofile_page(self):
        page = self.client.get("/userprofile/")
        self.assertTrue(page.status_code, 200)
        self.assertTemplateUsed(template_name='userprofile.html')

    def test_get_random_page(self):
        page = self.client.get("/randompage/")
        self.assertTrue(page.status_code, 404)
       
        


    

