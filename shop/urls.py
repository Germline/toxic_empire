from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin  # Import the admin module
from django.urls import path

from . import views

urlpatterns = (
    [
        path("", views.home, name="home"),
        path("shop", views.shop, name="shop"),
        path("contact", views.contact, name="contact"),
        path("login/", views.login_view, name="login"),
        path("register/", views.register, name="register"),
        path("logout/", views.logout_view, name="logout"),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
