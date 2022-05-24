from django.forms.widgets import TextInput


class PhoneInput(TextInput):
    """Define a telephone input class for use with phone numbers"""

    input_type = "tel"
