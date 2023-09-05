from django.urls import path
from . import views

app_name = "login"

urlpatterns = [
    path('signin', views.signin, name="connection"),
    path('signup', views.signup, name="register"),
    path('disconnect', views.disconnect, name="disconnect")
]

