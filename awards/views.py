from django.shortcuts import render, redirect
from .forms import RegisterForm, RateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Website, Rate

# Create your views here.

def home(request):
    title = "Home Page"
    cards = Website.get_all()
    return render(request, 'index.html' ,{"title": title, "cards": cards})

def site(request, pk):
    title= "site"
    photo = Website.objects.get(id=pk)

    site = Website.objects.get(id=pk)
    rates = Rate.objects.filter(website=site)
    rates_avg =

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


    return render(request, 'site.html', {"title": title, "photo": photo, "form":form})




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

