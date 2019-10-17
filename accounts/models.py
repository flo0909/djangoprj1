from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user_images')
    def __str__(self):
        return self.user.username +"'s" + ' ' + 'Profile'
