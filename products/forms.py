from django import forms

from .widgets import CustomClearableFileInput
from .models import Gender, Product, Category, Brand


class ProductForm(forms.ModelForm):
    """
    Form that allows store owners/staff to add products to Eau Royal
    database
    """

    class Meta:
        model = Product
        fields = "__all__"

    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        brands = Brand.objects.all()
        genders = Gender.objects.all()
        category_names = [(c.id, c.get_friendly_name()) for c in categories]
        brand_names = [(b.id, b.get_friendly_name()) for b in brands]
        gender_names = [(g.id, g.get_friendly_name()) for g in genders]

        self.fields["category"].choices = category_names
        self.fields["brand"].choices = brand_names
        self.fields["gender"].choices = gender_names
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "stripe-style-input"
