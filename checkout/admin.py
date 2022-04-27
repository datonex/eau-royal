from django.contrib import admin
from .models import Order, CartItem


class CartItemAdminInline(admin.TabularInline):
    model = CartItem
    readonly_fields = (
        "cartitem_price",
        "cartitem_total",
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (CartItemAdminInline,)

    readonly_fields = (
        "order_number",
        "date",
        "delivery_cost",
        "order_total",
        "total",
        "original_bag",
        "stripe_pid",
    )

    fields = (
        "order_number",
        "user_profile",
        "date",
        "full_name",
        "email",
        "phone_number",
        "country",
        "postcode",
        "town_or_city",
        "street_address1",
        "street_address2",
        "county",
        "delivery_cost",
        "order_total",
        "total",
        "original_bag",
        "stripe_pid",
    )

    list_display = (
        "order_number",
        "date",
        "full_name",
        "order_total",
        "delivery_cost",
        "total",
    )

    ordering = ("-date",)
