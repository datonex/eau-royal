from django.shortcuts import (
    redirect,
    render,
    reverse,
    get_object_or_404,
    HttpResponse,
)
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """View to return the shopping bag contents page"""

    template = "bag/bag.html"
    return render(request, template)


def add_to_bag(request, item_id):
    """Add a new item to the shopping bag"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    size = None

    if "product_size" in request.POST:
        size = request.POST["product_size"]

    bag = request.session.get("bag", {})
    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]["items_by_size"].keys():
                bag[item_id]["items_by_size"][size] += quantity
                messages.success(
                    request,
                    (
                        f"Updated size {size} "
                        f"{product.brand.name}, "
                        f"{product.name} {product.category.name} "
                        f"quantity to "
                        f'{bag[item_id]["items_by_size"][size]}'
                    )
                )
            else:
                bag[item_id]["items_by_size"][size] = quantity
                messages.success(
                    request,
                    (
                        f"Added size {size} "
                        f"{product.brand.name}, {product.name} "
                        f"{product.category.name} to your bag"
                    )
                )
        else:
            bag[item_id] = {"items_by_size": {size: quantity}}
            messages.success(
                request,
                (
                    f"Added size {size} "
                    f"{product.brand.name}, {product.name} "
                    f"{product.category.name} to your bag"
                )
            )
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                request,
                (
                    f"Updated {product.brand.name}, {product.name} "
                    f"{product.category.name} "
                    f"quantity to {bag[item_id]}"
                )
            )
        else:
            bag[item_id] = quantity
            messages.success(
                request,
                (
                    f"Added {product.brand.name}, {product.name} "
                    f"{product.category.name} to your bag"
                )
            )

    request.session["bag"] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Edit the quantity of a product to specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    size = None

    if "product_size" in request.POST:
        size = request.POST["product_size"]

    bag = request.session.get("bag", {})
    if size:
        if quantity > 0:
            bag[item_id]["items_by_size"][size] = quantity
            messages.success(
                request,
                (
                    f"Updated size {size} "
                    f"{product.brand.name}, {product.name} "
                    f"{product.category.name} quantity to "
                    f'{bag[item_id]["items_by_size"][size]}'
                )
            )
        else:
            del bag[item_id]["items_by_size"][size]
            if not bag[item_id]["items_by_size"]:
                bag.pop(item_id)
            messages.success(
                request,
                (
                    f"Removed size {size} "
                    f"{product.brand.name}, {product.name} "
                    f"{product.category.name} from your bag"
                )
            )
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request,
                (
                    f"Updated {product.brand.name}, {product.name} "
                    f"{product.category.name} "
                    f"quantity to {bag[item_id]}"
                )
            )
        else:
            bag.pop(item_id)
            messages.success(
                request,
                (
                    f"Removed {product.brand.name}, {product.name} "
                    f"{product.category.name} "
                    f"from your bag"
                ),
            )

    request.session["bag"] = bag
    return redirect(reverse("view_bag"))


def remove_from_bag(request, item_id):
    """Remove item from bag"""
    try:
        size = None
        product = get_object_or_404(Product, pk=item_id)
        if "product_size" in request.POST:
            size = request.POST["product_size"]
        bag = request.session.get("bag", {})

        if size:
            del bag[item_id]["items_by_size"][size]
            if not bag[item_id]["items_by_size"]:
                bag.pop(item_id)
            messages.success(
                request,
                (
                    f"Removed size {size} "
                    f"{product.brand.name}, {product.name} "
                    f"{product.category.name} from your bag"
                )
            )
        else:
            bag.pop(item_id)
            messages.success(
                request,
                (
                    f"Removed {product.brand.name}, {product.name} "
                    f"from your bag"
                )
            )

        request.session["bag"] = bag
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f"Error removing item: {e}")
        return HttpResponse(status=500)
