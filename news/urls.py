"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='all_news'),
    path('<int:pk>/', views.news_detail, name='news_detail'),
    path('new/', views.news_new, name='news_new'),
    path('<int:pk>/edit/', views.news_edit, name='news_edit'),
    path('<int:pk>/delete/', views.news_delete, name='news_delete'),
    path('tag/<int:pk>/', views.tag_detail_view, name='news_by_tag'),
]
