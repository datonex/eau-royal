from django.shortcuts import render


def index(request):
    """View to return homepage"""

    template = "home/index.html"
    return render(request, template)


def error_404(request, exception):
    return render(request, "errors/404.html")


def error_500(request, exception=None):
    return render(request, "errors/500.html")
