from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from auth_user.forms import RegisterForm, LoginForm
from auth_user.models import User


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "html/register.html", {"form": form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = User.objects.create_user(username=email, first_name=first_name, last_name=last_name, email=email,
                                            password=password)
            return redirect("login")
        else:
            return render(request, "html/register.html", {"form": form})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "html/login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("main")
            else:
                if len(User.objects.filter(username=username)) != 0:
                    error = "Błędne hasło"
                    return render(request, "html/login.html", {"form": form, "error": error})
                else:
                    return redirect("register")
        else:
            return render(request, "html/login.html", {"form": form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("main")
