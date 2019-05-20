"""Defines URL patterns for users."""

from django.contrib.auth import views as auth_views
from django.urls import path

from users import views

urlpatterns = [
    # login page
    path("login/", auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),

    # registration page
    path("register/", views.register, name="register"),

    # logout page
    path("logout/", auth_views.LogoutView.as_view(), name="logout")
]
