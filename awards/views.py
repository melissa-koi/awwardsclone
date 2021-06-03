from django.db.models import Avg, F, Sum
from django.shortcuts import render, redirect
from .forms import RegisterForm, RateForm, UploadWeb, CreateProfileForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Website, Rate,Profile
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url='/login/')
def home(request):
    title = "Home Page"
    cards = Website.get_all()
    return render(request, 'index.html' ,{"title": title, "cards": cards})

@login_required(login_url='/login/')
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

@login_required(login_url='/login/')
def post_website(request):
    current_user = request.user
    print(current_user)
    if request.method == "POST":
        form = UploadWeb(request.POST, request.FILES)
        if form.is_valid():
            img = form.save(commit=False)
            img.author =current_user
            img.save()
        return redirect('home')
    else:
        form = UploadWeb()
    return render(request, 'post_website.html', {"form":form})

@login_required(login_url='/login/')
def profile(request,username):
    title="profile"
    site = Website.get_user(username)
    profile =  Profile.get_user(username)
    print(request.user)
    return render(request, 'profile.html', {"title": title, "cards":site, "profiles":profile})

@login_required(login_url='/login/')
def update_profile(request,profile_id):
    user=User.objects.get(pk=profile_id)
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f"You Have Successfully Updated Your Profile!")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request,'update_profile.html',{"u_form":u_form, "p_form":p_form})

@login_required(login_url='/login/')
def search_results(request):
    if 'projects' in request.GET and request.GET["projects"]:
        search_term = request.GET.get("projects")
        searched_project = Website.get_projects(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{"message":message,"cards": searched_project})

    else:
        message = "You haven't searched for any term"
    return render(request, 'search.html',{"message":message})


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

