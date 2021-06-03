from django.db import models
from cloudinary.models import CloudinaryField
import datetime as dt
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    bio = models.TextField(blank=True)
    contact = models.CharField(max_length=20, blank=True)
    picture = CloudinaryField('photos',default='default.jpg')
    location = models.TextField(max_length=30, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        """Return username"""
        return self.user.username

    @classmethod
    def get_user(cls,username):
        profile = cls.objects.filter(user__username__icontains=username)
        return profile

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

class Website(models.Model):
    website = models.URLField(max_length=1000)
    location = models.TextField(max_length=30)
    image = CloudinaryField('photos')
    title = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE, null=True)

    def __str__(self):
        """Return username"""
        return self.author.username

    @classmethod
    def get_user(cls,username):
        user = cls.objects.filter(author__username__icontains=username)
        return user

    @classmethod
    def get_projects(cls,name):
        return cls.objects.filter(title__icontains=name)

    @classmethod
    def user_projects(cls,profile):
        return cls.objects.filter(profile=profile)

    @classmethod
    def get_all(cls):
        websites = cls.objects.all()
        return websites

RATE_CHOICES = [(1,'1'), (2,'2'), (3,'3'), (4,'4'), (5,'5'), (6,'6'), (7,'7'), (8,'8'), (9,'9'), (10,'10'), ]

class Rate(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    website = models.ForeignKey(Website, on_delete=models.CASCADE, null=True)
    creativity = models.PositiveSmallIntegerField(choices = RATE_CHOICES ,null=True)
    content = models.PositiveSmallIntegerField(choices = RATE_CHOICES,null=True)
    design = models.PositiveSmallIntegerField(choices = RATE_CHOICES,null=True)
    usability= models.PositiveSmallIntegerField(choices = RATE_CHOICES,null=True)

    def __str__(self):
        """Return username"""
        return self.user.username

