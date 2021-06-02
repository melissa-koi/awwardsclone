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
    path('profile/<str:username>/', views.profile, name = 'profile'),
    path('post/', views.post_website, name = 'post_website'),
    path('profile/update/<int:profile_id>/', views.update_profile, name='update_profile'),
    path('search/', views.search_results, name = 'search_results'),
]
