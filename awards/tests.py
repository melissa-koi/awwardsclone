from django.test import TestCase
from datetime import datetime
from .models import Profile, Website, Rate
from django.contrib.auth.models import User

# Create your tests here.


class TestUser (TestCase):
    def setUp(self):
        self.name = User(username='somename')
        self.name.save()

    def tearDown(self):
        User.objects.all().delete()

    def test_instance(self):
        self.assertEqual(self.name.username, 'somename')
        self.assertTrue(isinstance(self.name, User))


class TestUserProfile (TestCase):
    def setUp(self):
        self.name = User(username='somename')
        self.name.save()
        self.lord_stark = Profile(user=self.name, contact='1234',
                                  picture='pic.png', location='someniceplace', bio='bio')
        self.lord_stark.save(self.name)

    def tearDown(self):
        Profile.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.lord_stark, Profile))

    def test_save_profile(self):
        self.lord_stark.save(self.name)
        self.assertTrue(len(Profile.objects.all()) > 0)

class TestWebsiteTest(TestCase):
    def setUp(self):
        self.user=User.objects.create(username='name')
        self.user.save()
        self.project=Website.objects.create(id=1,title='somename',description='desc',image='image.png',urls='https://www.google.com/',profile=self.user)

    def tearDown(self):
        Website.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.project, Website))

    def test_save_project(self):
        self.project.save_project()
        total_proj=Website.objects.all()
        self.assertEqual(len(total_proj),1)

