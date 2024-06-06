from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.shortcuts import redirect, render

from .forms import RegisterForm
from .models import ContactMessage, Product

# Create your views here.


def base(request):
    return render(request, "base.html")


def home(request):
    products = Product.objects.all()
    return render(request, "index.html")


def shop(request):
    products = Product.objects.all()
    return render(request, "shop.html", {"products": products})


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        ContactMessage.objects.create(name=name, email=email, message=message)
        return redirect("contact")
    return render(request, "contact.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("home")  # Redirect to a success page
        else:
            return render(
                request, "login.html", {"error": "Invalid username or password"}
            )
    else:
        return render(request, "login.html")


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("login")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("home")
