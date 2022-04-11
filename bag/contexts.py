from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    sub_total = 0
    product_count = 0
    bag = request.session.get("bag", {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        sub_total += quantity * product.price
        product_count += quantity
        bag_items.append(
            {
                "item_id": item_id,
                "quantity": quantity,
                "product": product,
            }
        )

    if sub_total >= settings.DISCOUNT_THRESHOLD:
        discount = sub_total * Decimal(settings.DISCOUNT_PERCENTAGE / 100)
        discount_delta = settings.DISCOUNT_THRESHOLD - sub_total
    else:
        discount = 0
        discount_delta = 0

    total = discount + sub_total

    context = {
        "bag_items": bag_items,
        "product_count": product_count,
        "sub_total": sub_total,
        "total": total,
        "discount": discount,
        "discount_delta": discount_delta,
        "discount_threshold": settings.DISCOUNT_THRESHOLD,
        "discount_percentage": settings.DISCOUNT_PERCENTAGE,
    }

    return context
