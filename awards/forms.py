from django import forms
from .models import Website, RATE_CHOICES, Rate
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
        fields = ['rate', ]
