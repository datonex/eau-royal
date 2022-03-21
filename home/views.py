from django.shortcuts import render


def index(request):
    """View to return homepage"""

    template = "home/index.html"
    return render(request, template)
