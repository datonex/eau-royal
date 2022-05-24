from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .models import Order, CartItem
from products.models import Product
from profiles.models import UserProfile

import json
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        cust_email = order.email
        subject = render_to_string(
            "checkout/confirmation_emails/confirmation_email_subject.txt",
            {"order": order},
        )
        body = render_to_string(
            "checkout/confirmation_emails/confirmation_email_body.txt",
            {"order": order, "contact_email": settings.DEFAULT_FROM_EMAIL},
        )

        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [cust_email])

    def handle_event(self, event):
        """Handle generic/unknown/unexpected webhook event"""

        return HttpResponse(content=f"Webhook received: {event['type']}",
                            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        address_line_1 = shipping_details.address.line1
        address_line_2 = shipping_details.address.line2

        if username != "AnonymousUser":
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = shipping_details.phone
                profile.default_street_address1 = address_line_1
                profile.default_street_address2 = address_line_2
                profile.default_town_or_city = shipping_details.address.city
                profile.default_county = shipping_details.address.state
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_country = shipping_details.address.country
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.full_name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    town_or_city__iexact=shipping_details.address.city,
                    county__iexact=shipping_details.address.state,
                    postcode__iexact=shipping_details.address.postal_code,
                    country__iexact=shipping_details.address.country,
                    total=total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True

            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=(f"Webhook received: {event['type']} "
                         f"| SUCCESS: Verified order already in database"),
                status=200,
            )
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.full_name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    town_or_city=shipping_details.address.city,
                    county=shipping_details.address.state,
                    postcode=shipping_details.address.postal_code,
                    country=shipping_details.address.country,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_cart_item = CartItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                            product_size=size,
                        )
                        order_cart_item.save()
                    else:
                        item_data_items = item_data["items_by_size"].items()
                        for size, quantity in item_data_items:
                            order_cart_item = CartItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                        order_cart_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f"Webhook received: {event['type']} | ERROR: {e}",
                    status=500,
                )

        self._send_confirmation_email(order)
        return HttpResponse(
            content=(f"Webhook received: {event['type']} "
                     f"| SUCCESS: Created order in webhook"),
            status=200,
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(content=f"Webhook received: {event['type']}",
                            status=200)
