# users/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Index sahifasi uchun URL
    path('login/', views.login_view, name='login'),
]
