from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, get_user_model
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import CustomUser


def signin(request):
    form = AuthenticationForm
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("login:profile")
        else:
            messages.info(request, "login ou mot de passe incorrect !")
            return redirect("login:connection")

    return render(request, "login_views/login.html", context={"form": form})


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password != password2:
            return render(request, "login_views/signup.html", context={'error': "Nom d'utilisateur ou mot de passe incorrect"})
        user = CustomUser.objects.create_user(username=username, password=password, email=email)
        login(request, user)
        return redirect("login:profile")
    return render(request, 'login_views/signup.html')





def disconnect(request):
    logout(request)
    messages.info(request, "Vous êtes déconnecté !")
    return redirect("home")


def profile(request):
    return render(request, "login_views/profile.html")
