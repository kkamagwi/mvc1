from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="account/registration/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="account/registration/logged_out.html"), name='logout'),
    path('', views.dashboard, name='dashboard'),
]