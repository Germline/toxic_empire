from django.contrib import admin

from .models import ContactMessage, Product

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "price", "image"]


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ContactMessage._meta.fields]
