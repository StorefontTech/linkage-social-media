from typing import Optional

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from users.forms import CreateUserForm
from users.models import User


# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user: Optional[User] = authenticate(request, username=username, password=password)

        if user is None:
            context = {"error": "Username or Password is incorrect"}
            return render(request, "users/login.html", context)

        login(request, user)
        return redirect("/")

    return render(request, "users/login.html")


def register_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    form: CreateUserForm = CreateUserForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' is-invalid active'

    return render(request, "users/register.html", {"form": form})
