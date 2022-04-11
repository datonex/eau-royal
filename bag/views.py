from django.shortcuts import render

from django.shortcuts import render


def view_bag(request):
    """View to return the shopping bag content"""

    template = "bag/bag.html"
    return render(request, template)
