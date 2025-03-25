from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, redirect
from .models import ShortUrl
from .serializers import UrlSeri


@api_view(["POST"])
def shorten_url(request):
    """API to shorten a given URL"""
    serializer = UrlSeri(data=request.data)
    if serializer.is_valid():
        org_url = serializer.validated_data["org_url"]
        short_url_obj, created = ShortUrl.objects.get_or_create(org_url=org_url)
        return Response(
            {"short_url": f"http://127.0.0.1:8000/shortly/{short_url_obj.short_url}"},
            status=status.HTTP_201_CREATED,
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def redirect_to_original(request, short_url):
    """Redirects short URL to the original URL"""
    url_instance = get_object_or_404(ShortUrl, short_url=short_url)
    return redirect(url_instance.org_url)


@api_view(["GET"])
def get_all_shortened_urls(request):
    """Fetch all shortened URLs"""
    urls = ShortUrl.objects.all()
    serializer = UrlSeri(urls, many=True)
    return Response(serializer.data)
