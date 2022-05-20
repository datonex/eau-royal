from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from products.models import Brand


def get_price(product, key):
    price_dictionary = {
        "30ML": product.price / 3,
        "50ML": product.price,
        "100ML": product.price * 2,
        "onesize": product.price,
    }
    return price_dictionary[key]


def bag_contents(request):
    bag_items = []
    sub_total = 0
    product_count = 0
    bag = request.session.get("bag", {})
    brands = Brand.objects.all()

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            size = "onesize"
            price = get_price(product, size)
            sub_total += item_data * price
            product_count += item_data
            bag_items.append(
                {
                    "item_id": item_id,
                    "quantity": item_data,
                    "product": product,
                    "item_price": price,
                    "item_total": price * item_data,
                    "size": size,
                }
            )
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data["items_by_size"].items():
                price = get_price(product, size)
                sub_total += quantity * price
                product_count += quantity
                bag_items.append(
                    {
                        "item_id": item_id,
                        "quantity": quantity,
                        "product": product,
                        "item_price": price,
                        "item_total": price * quantity,
                        "size": size,
                    }
                )

    if sub_total >= settings.DISCOUNT_THRESHOLD:
        discount = sub_total * Decimal(settings.DISCOUNT_PERCENTAGE / 100)
        discount_delta = 0
    else:
        discount = 0
        discount_delta = settings.DISCOUNT_THRESHOLD - sub_total

    pre_delivery = sub_total - discount
    delivery_price = Decimal(5.99)
    if pre_delivery < settings.FREE_DELIVERY_THRESHOLD:
        delivery = delivery_price
    else:
        delivery = 0

    total = pre_delivery + delivery

    context = {
        "bag_items": bag_items,
        "product_count": product_count,
        "meta_brands": brands,
        "sub_total": sub_total,
        "total": total,
        "discount": discount,
        "discount_delta": discount_delta,
        "delivery": delivery,
        "delivery_price": delivery_price,
        "pre_delivery": pre_delivery,
        "delivery_threshold": settings.FREE_DELIVERY_THRESHOLD,
        "discount_threshold": settings.DISCOUNT_THRESHOLD,
        "discount_percentage": settings.DISCOUNT_PERCENTAGE,
    }

    return context
