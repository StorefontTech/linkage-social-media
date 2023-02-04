from typing import Optional

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from users.models import User


# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect("/")

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
