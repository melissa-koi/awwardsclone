from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.home), name = 'home'),
    path('register/', views.registerUser, name = 'register'),
    path('login/', views.loginUser, name = 'login'),
    path('logout/', views.logoutUser, name = 'logout'),
    path('site/<str:pk>/', login_required(views.site), name = 'site'),
    path('profile/<str:username>/', login_required(views.profile) , name = 'profile'),
    path('post/', login_required(views.post_website) , name = 'post_website'),
    path('profile/update/<int:profile_id>/', login_required(views.update_profile) , name='update_profile'),
    path('search/', login_required(views.search_results), name = 'search_results'),
]
