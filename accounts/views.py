from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm, LoginForm

def home(request):
    return render(request, 'accounts/home.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('core:dashboard')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def user_login(request):
    form = LoginForm(request)
    error = None

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        print("Форма подадена с данни:", request.POST)  # Проверяваме входните данни

        if form.is_valid():
            user = form.get_user()
            print("Форма валидна, намерен потребител:", user)

            if user is not None:
                print("Логваме потребителя:", user.username)
                login(request, user)
                return redirect('core:dashboard')
            else:
                print("Форма е валидна, но потребителят е None?!")
                error = "Unexpected error, please try again."
        else:
            print("Форма НЕ е валидна!")
            print("Грешки:", form.errors.as_json())  # По-детайлна грешка

            error = "Invalid username or password"

    return render(request, 'accounts/login.html', {'form': form, 'error': error})


def user_logout(request):
    logout(request)
    return redirect('home')
