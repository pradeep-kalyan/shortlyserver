from django.urls import path
from .views import shorten_url, redirect_to_original, get_all_shortened_urls

urlpatterns = [
    path("shorten/", shorten_url, name="shorten_url"),  # API to shorten a URL
    path(
        "<str:short_url>/", redirect_to_original, name="redirect_to_original"
    ),  # Redirect to original URL
    # path("urls/", get_all_shortened_urls, name="get_all_shortened_urls"),  # Fetch all shortened URLs
]
