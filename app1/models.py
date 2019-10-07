from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class UserPost(models.Model):
    name = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    done = models.BooleanField(default=False)
    votes = models.IntegerField(default=0)
    voted = models.TextField()
    def __str__(self):
        return self.name
        
class Answer(models.Model):
    name = models.CharField(max_length=250)
    content = models.TextField()
    answered_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.name)