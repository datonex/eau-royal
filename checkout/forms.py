from django import forms
from django.forms.widgets import TextInput

from .models import Order


class PhoneInput(TextInput):
    """Define a telephone input class for use with phone numbers"""

    input_type = "tel"


class OrderForm(forms.ModelForm):
    """
    Form Class that renders a form to the user so that their order
    can be sent to the database
    """

    class Meta:
        model = Order
        fields = (
            "full_name",
            "email",
            "phone_number",
            "street_address1",
            "street_address2",
            "town_or_city",
            "county",
            "postcode",
            "country",
        )

        widgets = {
            "full_name": forms.TextInput(
                attrs={
                    "pattern": "/^[a-zA-Z-']+ [a-zA-Z-']+$/",
                    "title": "Please enter your FULL name",
                    "autocomplete": "name",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "pattern": "/^[a-zA-Z0-9._-]+@[a-zA-Z]+\.[a-zA-Z]+$/",
                    "title": ("Please enter your email in the format: "
                              "email@example.com"),
                    "autocomplete": "email",
                }
            ),
            "phone_number": PhoneInput(
                attrs={
                    "pattern": ("/^\+[1-9]\d{2}\d{10}|\+[1-9][0-9]\d{10}"
                                "|0?1?8?\d{4,15}$/"),
                    "title": "Please enter a valid phone number in "
                    "the format: 0123456789 or +12345678912",
                    "autocomplete": "tel",
                }
            ),
            "street_address1": forms.TextInput(
                attrs={
                    "pattern": ("/^[a-zA-Z0-9-.']+ [a-zA-Z0-9-.']+ "
                                "[a-zA-Z0-9-.']+$/"),
                    "title": "Please enter a valid address",
                    "autocomplete": "address-line1",
                }
            ),
            "town_or_city": forms.TextInput(
                attrs={
                    "pattern": "/^[a-zA-Z-.' ]+$/",
                    "title": "Please enter a valid town or city",
                    "autocomplete": "address-level1",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        """
        Initialisation function that adds placeholders and classes and
        remove auto-generated labels and set autofocus on first field
        """

        super().__init__(*args, **kwargs)
        placeholders = {
            "full_name": "Full Name",
            "email": "Email Address",
            "phone_number": "Phone Number",
            "street_address1": "Street Address 1",
            "street_address2": "Street Address 2",
            "town_or_city": "Town or City",
            "county": "County, State or Locality",
            "postcode": "Postal Code",
        }

        self.fields["full_name"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if field != "country":
                if self.fields[field].required:
                    placeholder = f"{placeholders[field]} *"
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].widget.attrs["class"] = "stripe-style-input"
            self.fields[field].label = False
