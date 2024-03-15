# baby urls

from django.urls import path
from . import views

app_name = 'flyapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('meetTheTeam/', views.meetTheTeam, name='meetTheTeam'),
    path('register_customer/', views.register_customer, name='register_customer'),
    path('login/', views.login_customer, name='login_customer'),
    path('logout/', views.logout_customer, name='logout_customer'),    
]
