from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.

class Website(models.Model):
    website = models.URLField(max_length=1000)
    location = models.TextField(max_length=30)
    image = CloudinaryField('photos')
    title = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        """Return username"""
        return self.author.username

    