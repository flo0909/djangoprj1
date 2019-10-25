from django.test import TestCase
from .forms import TicketForm
from app1.models import Answer

# Create your tests here.
class TestForms(TestCase):

    def test_create_with_author(self):
        form = TicketForm({'author': 'Myself'})
        self.assertFalse(form.is_valid())

    def test_create_with_name(self):
        form = TicketForm({'name': 'Myself'})
        self.assertFalse(form.is_valid())
    
    def test_no_input(self):
        form = TicketForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], ['This field is required.'])

class TestViews(TestCase):

    def test_get_list_page(self):
        page = self.client.get("/ticketlist/")
        self.assertTrue(page.status_code, 200)
        self.assertTemplateUsed(template_name='ticketlist.html')
        

    def test_get_answer_page(self):
        page = self.client.get("/ticketanswer/")
        self.assertTrue(page.status_code, 200)
        self.assertTemplateUsed(template_name='ticketanswer.html')
        
    def test_get_details_page(self):
        page = self.client.get("/ticketdetail/")
        self.assertTrue(page.status_code, 200)
        self.assertTemplateUsed(template_name='ticketdetail.html')

    def test_get_update_page(self):
        page = self.client.get("/ticketupdate/")
        self.assertTrue(page.status_code, 200)
        self.assertTemplateUsed(template_name='ticketupdate.html')

    def test_get_done_page(self):
        page = self.client.get("/ticketdone/")
        self.assertTrue(page.status_code, 200)
        self.assertTemplateUsed(template_name='ticketdone.html')

    def test_get_random_page(self):
        page = self.client.get("/randompage/")
        self.assertTrue(page.status_code, 404)
       
        

class TestModels(TestCase):

    def test_answer_model(self):
        post = Answer(name="Answer to Ticket")
        post.save()
        self.assertEqual(post.name, "Answer to Ticket")
        self.assertTrue(post.name, "Answer to Ticket")
    
    def test_create_answer(self):
        post = Answer(name="Create Answer", content='content')
        post.save()
        self.assertEqual(post.name, "Create Answer")
        self.assertEqual(post.content, "content")
        self.assertTrue(post.name, "Create Answer")