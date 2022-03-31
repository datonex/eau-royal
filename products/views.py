from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Product


def all_products(request):
    """View function that returns all products, including search and sorting queries"""

    template = "products/products.html"

    products_list = Product.objects.all()
    paginator = Paginator(products_list, 60)
    page_number = request.GET.get("page")

    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        "products": products,
    }

    return render(request, template, context)


def product_detail(request, product_id):
    """View function that returns individual product details"""

    template = "products/product_detail.html"
    product = get_object_or_404(Product, pk=product_id)

    context = {
        "product": product,
    }

    return render(request, template, context)
