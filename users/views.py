from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth import logout
from .forms import CustomUserRegistrationForm
from django.contrib.auth import login

User = get_user_model()



def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "Email yoki parol noto‘g‘ri!")
            return render(request, 'register/login.html')

        auth_user = authenticate(request, username=user.username, password=password)
        if auth_user is not None:
            login(request, auth_user)
            return redirect('index')
        else:
            messages.error(request, "Email yoki parol noto‘g‘ri!")

    return render(request, 'register/login.html')

def index(request):
    return render(request, 'index.html')








def register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.profile.gender = form.cleaned_data['gender']
            user.profile.passport_number = form.cleaned_data['passport_number']
            user.profile.birth_date = form.cleaned_data['birth_date']
            user.profile.save()
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'register/register.html', {'form': form})
