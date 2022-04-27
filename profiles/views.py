from django.shortcuts import render, get_object_or_404

from .models import UserProfile


def profile(request):
    """View to return the users's profile information"""

    profile = get_object_or_404(UserProfile, user=request.user)

    template = "profile/profile.html"
    context = {
        "profile": profile,
    }

    return render(request, template, context)
