from django.test import TestCase
from .forms import PostForm
from . models import Answer

# Create your tests here.
class TestForms(TestCase):

    def test_create_with_author(self):
        form = PostForm({'author': 'Myself'})
        self.assertFalse(form.is_valid())

    def test_create_with_name(self):
        form = PostForm({'name': 'Myself'})
        self.assertFalse(form.is_valid())
    
    def test_no_input(self):
        form = PostForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], ['This field is required.'])

class TestViews(TestCase):

    def test_get_index_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "app1/index.html")

    def test_get_list_page(self):
        page = self.client.get("/postslist/")
        self.assertTrue(page.status_code, 200)
        self.assertTemplateUsed(template_name='postslist.html')
    
    def test_get_details_page(self):
        page = self.client.get("/postdetail/")
        self.assertTrue(page.status_code, 200)
        self.assertTemplateUsed(template_name='postdetail.html')

    def test_get_answer_page(self):
        page = self.client.get("/postanswer/")
        self.assertTrue(page.status_code, 200)
        self.assertTemplateUsed(template_name='postanswer.html')

    def test_get_update_page(self):
        page = self.client.get("/postupdate/")
        self.assertTrue(page.status_code, 200)
        self.assertTemplateUsed(template_name='postupdate.html')
            

    def test_get_random(self):
        page = self.client.get("/random/")
        self.assertEqual(page.status_code, 404)
        

class TestModels(TestCase):

    def test_check_name(self):
        post = Answer(name="Answer to Post")
        post.save()
        self.assertEqual(post.name, "Answer to Post")
        self.assertTrue(post.name, "Answer to Post")
    
    def test_create(self):
        post = Answer(name="Answer to Post", content='content')
        post.save()
        self.assertEqual(post.name, "Answer to Post")
        self.assertEqual(post.content, "content")
        self.assertTrue(post.name, "Answer to Post")
