from django.contrib import admin
from .models import Brand, Category, Product


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
    )

    ordering = ("sku",)


@admin.register(Category)
@admin.register(Brand)
class DatabaseAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "db_name",
    )

    ordering = ("id",)
