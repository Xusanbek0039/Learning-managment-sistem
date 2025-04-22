from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Jet admin paneli uchun
    path('admin/', admin.site.urls),
    path('', include('users.urls')),  # myapp URL-larini qo'shish
]