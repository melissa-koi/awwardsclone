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
    description = models.TextField(null=True)
    def __str__(self):
        """Return username"""
        return self.author.username

    @classmethod
    def get_all(cls):
        websites = cls.objects.all()
        return websites

RATE_CHOICES = [(1,'1'), (2,'2'), (3,'3'), (4,'4'), (5,'5'), (6,'6'), (7,'7'), (8,'8'), (9,'9'), (10,'10'), ]

class Rate(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    website = models.ForeignKey(Website, on_delete=models.CASCADE, related_name="comments", null=True)
    design = models.PositiveSmallIntegerField(choices = RATE_CHOICES, blank=True)
    usability = models.PositiveSmallIntegerField(choices = RATE_CHOICES, blank=True)
    creativity = models.PositiveSmallIntegerField(choices = RATE_CHOICES, blank=True)
    content = models.PositiveSmallIntegerField(choices = RATE_CHOICES, blank=True)

    def __str__(self):
        """Return username"""
        return self.user.username
