from django.urls import path
from . import views


urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(template_name="account/registration/login.html"), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name="account/registration/logged_out.html"), name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    # path('edit/', views.edit, name='edit_account'),
]