from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def signup_page(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():

            return render(
                request,
                "accounts/signup.html",
                {
                    "error": "Username already exists"
                }
            )

        user = User.objects.create_user(
            username=username,
            password=password
        )

        login(request, user)

        return redirect("/")

    return render(
        request,
        "accounts/signup.html"
    )


def login_page(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("/")

        return render(
            request,
            "accounts/login.html",
            {
                "error": "Invalid username or password"
            }
        )

    return render(
        request,
        "accounts/login.html"
    )


def logout_page(request):

    logout(request)

    return redirect("/")