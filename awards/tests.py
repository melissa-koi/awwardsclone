from django.test import TestCase
from datetime import datetime
from .models import Profile, Website, Rate
from django.contrib.auth.models import User

# Create your tests here.


class TestUserProfile (TestCase):

    def setUp(self):
        self.name = User(username='somename' ,email='name@gmail.com')
        self.name.save()
        self.lord_stark = Profile(user=self.name, contact='1234',
                                  picture='pic.png', location='someniceplace', bio='bio')

    def tearDown(self):
        Profile.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.lord_stark, Profile))

    def test_save_profile(self):
        self.lord_stark.save_profile
        self.assertTrue(len(Profile.objects.all()) > 0)

    def test_delete_profile(self):
        self.lord_stark.save_profile
        profile = Profile.objects.all()
        self.lord_stark.delete_profile()
        self.assertTrue(len(profile) < 1)

class TestWebsiteTest(TestCase):
    def setUp(self):
        self.name = User(username='somename' ,email='name@gmail.com')
        self.name.save()
        self.site=Website(author=self.name ,title='somename',description='desc',image='image.png',website='https://www.google.com/',profile=self.user, location='Dubai')

    def tearDown(self):
        Website.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.project, Website))

    def test_save_project(self):
        self.project.save()
        projects=Website.objects.all()
        self.assertEqual(len(projects),1)

