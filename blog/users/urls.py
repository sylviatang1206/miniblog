from django.urls import path
from . import views
from .models import User

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('welcome', views.welcome),
    path('welcome_user', views.welcomeUser, name="welcome_user"),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin),
    path('signout', views.signout),
    path('admin1', views.admin1),
    path('delete_user/<pk>', views.delete_user, name="delete_user"),
    path('update_user', views.update_user, name="update_user"),
    path('create_user', views.create_user, name="create_user"),
    
]
