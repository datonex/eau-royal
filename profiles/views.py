from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """View to return the users's profile information"""

    profile = get_object_or_404(UserProfile, user=request.user)

    username = request.user.username
    user_initials = username[0] + username[-1]

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
        else:
            messages.error(
                request, ("Update failed." "Please ensure the form is valid.")
            )
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = "profile/profile.html"
    context = {
        "form": form,
        "orders": orders,
        "user_initials": user_initials,
        "on_profile_page": True,
    }

    return render(request, template, context)
