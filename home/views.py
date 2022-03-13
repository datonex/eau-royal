from django.shortcuts import render


def index(request):
    """View to return homepage"""

    context = "home/index.html"
    return render(request, context)
