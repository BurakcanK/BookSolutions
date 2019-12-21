from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def register(request):
    """Register a new user."""
    if request.method != "POST":
        # display blank registration form
        form = UserCreationForm()
    else:
        # process completed form
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("learning_logs:index")

    context = {"form": form}
    return render(request, "registration/register.html", context)
