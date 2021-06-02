from django import forms
from .models import Website, RATE_CHOICES, Rate, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password']

class RateForm(forms.ModelForm):

    class Meta:
        model = Rate
        fields = ['creativity','content', 'design', 'usability']

class UploadWeb(forms.ModelForm):
    class Meta:
        model = Website
        fields = ['website', 'location', 'image', 'title', 'description']

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class UserUpdateForm(forms.ModelForm):
    '''
    Form to update user profile
    '''
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    '''
    Form to update user profile picture
    '''

    class Meta:
        model = Profile
        fields = ['bio','contact', 'picture', 'location']


