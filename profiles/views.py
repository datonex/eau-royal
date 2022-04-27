from django.shortcuts import render


def profile(request):
    """View to return the users's profile information"""

    template = "profile/profile.html"
    context = {}

    return render(request, template, context)
