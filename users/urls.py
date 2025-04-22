from django.urls import path
from .views import index, login_view, register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name='index'),       # Bosh sahifa
    path('login/', login_view, name='login'),  # Login sahifasi
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', register, name='register'),  # <-- SHU YER TO‘G‘RILANDI
]
