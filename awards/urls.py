from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name = 'home'),
    path('register/', views.registerUser, name = 'register'),
    path('login/', views.loginUser, name = 'login'),
    path('logout/', views.logoutUser, name = 'logout'),
    path('site/<str:pk>/', views.site, name = 'site'),
]
