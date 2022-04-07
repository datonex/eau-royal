from logging import exception
from django.forms import ValidationError
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Product, Category, Gender


def all_products(request):
    """View function that returns all products, including search and sorting queries"""

    template = "products/products.html"

    products = Product.objects.all()
    total_products = products.count()

    query = None
    categories = None
    genders = None
    discounts = None
    sort = None
    direction = None

    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))
            if sortkey == "category":
                sortkey = "category__name"
            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)

        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            if not categories:
                messages.error(
                    request, (f"'{categories}' does not exist in Categories table")
                )
                return redirect(reverse("products"))

        if "gender" in request.GET:
            genders = request.GET["gender"].split(",")
            products = products.filter(gender__db_name__in=genders)
            genders = Gender.objects.filter(db_name__in=genders)
            if not genders:
                messages.error(request, (f"'{genders}' does not exist in Gender table"))
                return redirect(reverse("products"))

        if "has_discount" in request.GET:
            try:
                discounts = request.GET["has_discount"]
                products = products.filter(has_discount=discounts)
                discounts = Product.objects.filter(has_discount=discounts)
            except (ValidationError) as e:
                if isinstance(e, ValidationError):
                    messages.error(
                        request,
                        (
                            f"'{discounts}' is not a boolean value, please enter 'True' or 'False'"
                        ),
                    )
                    return redirect(reverse("products"))

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

    current_sorting = f"{sort}_{direction}"

    page_number = request.GET.get("page", 1)
    paginator = Paginator(products, 60)

    try:
        products = paginator.page(page_number)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    print(discounts)

    context = {
        "products": products,
        "total_products": total_products,
        "search_term": query,
        "current_categories": categories,
        "current_genders": genders,
        "current_discounts": discounts,
        "current_sorting": current_sorting,
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
