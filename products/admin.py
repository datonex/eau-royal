from django.contrib import admin
from .models import Brand, Category, Product, Gender


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "sku",
        "name",
        "brand",
        "category",
        "price",
        "rating",
        "image",
        "gender",
    )

    ordering = ("sku",)


@admin.register(Brand, Category, Gender)
class DatabaseAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "db_name",
    )

    ordering = ("id",)
