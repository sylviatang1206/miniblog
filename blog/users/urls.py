from django.urls import path
from . import views
from .models import User

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('signup', views.signup, name='signup'),
    path('welcome<>', views.welcomeUser, name="welcome_user"),
    path('signin', views.signin),
    path('signout', views.signout),
    path('admin1', views.admin1),
    path('get_users', views.get_users),
    path('update_user', views.update_user),
    path('delete_user', views.delete_user)
]
