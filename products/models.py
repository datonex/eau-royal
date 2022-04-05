from unicodedata import name
from django.db import models
import glob, os


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    db_name = models.CharField(max_length=254)
    name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.db_name

    def get_friendly_name(self):
        return self.name


class Gender(models.Model):
    class Meta:
        verbose_name_plural = "Genders"

    db_name = models.CharField(max_length=2)
    name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.db_name

    def get_friendly_name(self):
        return self.name


class Brand(models.Model):
    class Meta:
        verbose_name_plural = "Brands"

    db_name = models.CharField(max_length=254)
    name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.db_name

    def get_friendly_name(self):
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=254)
    brand = models.ForeignKey("Brand", null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True, unique=True)
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    gender = models.ForeignKey(
        "Gender", null=True, blank=True, on_delete=models.SET_NULL
    )
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    has_discount = models.BooleanField(default=False, null=True, blank=True)
    has_subscription = models.BooleanField(default=False, null=True, blank=True)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True, default=0
    )
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    scent = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name
