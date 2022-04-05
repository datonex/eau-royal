from dis import dis
from itertools import product
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q, F
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Product, Category, Gender


def all_products(request):
    """View function that returns all products, including search and sorting queries"""

    template = "products/products.html"

    products = Product.objects.all()

    query = None
    categories = None
    genders = None

    if request.GET:
        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
        if "gender" in request.GET:
            genders = request.GET["gender"].split(",")
            products = products.filter(gender__db_name__in=genders)
            genders = Gender.objects.filter(db_name__in=genders)
        if "has_discount" in request.GET:
            products = products.filter(has_discount=True)
        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, ("You didn't enter any search criteria!"))
                return redirect(reverse("products"))

            queries = (
                Q(name__icontains=query)
                | Q(description__icontains=query)
                | Q(brand__name__icontains=query)
                | Q(category__name__icontains=query)
            )
            products = products.filter(queries)

    page_number = request.GET.get("page", 1)
    paginator = Paginator(products, 60)

    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    context = {
        "products": products,
        "search_term": query,
        "homepage_filters": categories,
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
