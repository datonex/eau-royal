from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm


def checkout(request):
    """
    View to return user input when fillinf forms and handle stripe
    payments
    """

    template = "checkout/checkout.html"
    order_form = OrderForm()
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    bag = request.session.get("bag", {})
    details = request.session.get("details", {})
    delivery = request.session.get("delivery", {})
    first_name = None
    last_name = None
    email = None
    phone_number = None
    street_address1 = None
    street_address2 = None
    town_or_city = None
    county = None
    postcode = None
    country = None

    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse("products"))

    if "first_name" in request.POST:
        first_name = request.POST["first_name"]
        print(first_name)
        details["first_name"] = first_name
    if "last_name" in request.POST:
        last_name = request.POST["last_name"]
        print(last_name)
        details["last_name"] = last_name
    if "email" in request.POST:
        email = request.POST["email"]
        print(email)
        details["email"] = email
    if "phone_number" in request.POST:
        phone_number = request.POST["phone_number"]
        print(phone_number)
        details["phone_number"] = phone_number
    if "street_address1" in request.POST:
        street_address1 = request.POST["street_address1"]
        print(street_address1)
        delivery["street_address1"] = street_address1
    if "street_address2" in request.POST:
        street_address2 = request.POST["street_address2"]
        print(street_address2)
        delivery["street_address2"] = street_address1
    if "town_or_city" in request.POST:
        town_or_city = request.POST["town_or_city"]
        print(town_or_city)
        delivery["town_or_city"] = town_or_city
    if "county" in request.POST:
        county = request.POST["county"]
        print(county)
        delivery["county"] = county
    if "postcode" in request.POST:
        postcode = request.POST["postcode"]
        print(postcode)
        delivery["postcode"] = postcode
    if "country" in request.POST:
        country = request.POST["country"]
        print(country)
        delivery["country"] = country

    print(f"details dictionary: {details}")
    print(f"delivery dictionary: {delivery}")

    request.session["details"] = details
    request.session["delivery"] = delivery

    context = {
        "order_form": order_form,
        "details": details,
        "delivery": delivery,
        "stripe_public_key": stripe_public_key,
        "client_secret": "client secret",
    }

    return render(request, template, context)
