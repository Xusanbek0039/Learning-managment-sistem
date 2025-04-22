from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model

User = get_user_model()

def index(request):
    return render(request, 'index.html')  # index.html sahifasini ko'rsatish


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        if user is not None:
            auth_user = authenticate(request, username=user.username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect('index')  # yoki o'zing yo'naltirmoqchi bo'lgan sahifa
        messages.error(request, "Email yoki parol noto‘g‘ri!")

    return render(request, 'register/login.html')
