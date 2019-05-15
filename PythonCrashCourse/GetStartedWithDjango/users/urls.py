"""Defines URL patterns for users."""

from django.contrib.auth import login
from django.urls import path

from users import views

urlpatterns = [
    # login page
    path("login/", login, {"template_name": "users/login.html"}, name="login"),
]
