from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def signin(request):
    form = AuthenticationForm
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, "erreur de connexion, veuillez recommencer !")
            return redirect("www.facebook.com")
    return render(request, "login_views/login.html", context={"form": form})


def signup(request):
    return render(request, 'login_views/signup.html')


def disconnect(request):
    logout(request)
    return redirect("home")
