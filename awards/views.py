from django.db.models import Avg, F, Sum
from django.shortcuts import render, redirect
from .forms import RegisterForm, RateForm, UploadWeb, CreateProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Website, Rate,Profile

# Create your views here.

def home(request):
    title = "Home Page"
    print(request.user)
    cards = Website.get_all()
    return render(request, 'index.html' ,{"title": title, "cards": cards})

def site(request, pk):
    title= "site"
    photo = Website.objects.get(id=pk)

    site = Website.objects.get(id=pk)
    rates = Rate.objects.filter(website=site)
    user = request.user
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = user
            rate.website = site
            rate.save()
    else:
        form = RateForm()

    return render(request, 'site.html', {"title": title, "photo": photo, "form":form, "rates":rates})

def post_website(request):
    C_user = request.user
    if request.method == "POST":
        form = UploadWeb(request.POST, request.FILES)
        if form.is_valid():
            img = form.save(commit=False)
            img.author = C_user
            img.save()
        return redirect('home')
    else:
        form = UploadWeb()
    return render(request, 'post_website.html', {"form":form})

def profile(request,username):
    title="profile"
    site = Website.get_user(username)
    profile =  Profile.get_user(username)
    print(site)
    return render(request, 'profile.html', {"title": title, "cards":site, "profile":profile})

def create_profile(request):
    current_user=request.user
    if request.method == 'POST':
        form = CreateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
    else:
        form = CreateProfileForm()
    return render(request,'create_profile.html',{"form":form})

def registerUser(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form':form})

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Username or Password is Incorrect')
        else:
            messages.error(request, 'Fill out all the fields')

    return render(request, 'accounts/login.html', {})

def logoutUser(request):
    logout(request)
    return redirect('home')

