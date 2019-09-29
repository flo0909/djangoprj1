from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class UserPost(models.Model):
    name = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    votes = models.IntegerField(default=0)
    voted = models.TextField()
    def __str__(self):
        return self.name