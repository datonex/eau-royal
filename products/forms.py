from django import forms

from .widgets import CustomClearableFileInput
from .models import Gender, Product, Category, Brand


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        brand = Brand.objects.all()
        gender = Gender.objects.all()
        category_friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        brand_friendly_names = [(b.id, b.get_friendly_name()) for b in brand]
        gender_friendly_names = [(g.id, g.get_friendly_name()) for g in gender]

        self.fields["category"].choices = category_friendly_names
        self.fields["brand"].choices = brand_friendly_names
        self.fields["gender"].choices = gender_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "stripe-style-input"
