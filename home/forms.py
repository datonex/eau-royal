from django import forms
from .models import Subscriber


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ("email",)

    def __init__(self, *args, **kwargs):
        """
        Initialisation function that adds placeholders and classes and
        remove auto-generated labels and set autofocus on first field
        """

        super().__init__(*args, **kwargs)
        placeholders = {
            "email": "Email",
        }

        self.fields["email"].widget.attrs["autofocus"] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].widget.attrs["class"] = "stripe-style-input"
            self.fields[field].label = False
