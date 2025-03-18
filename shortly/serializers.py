from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import ShortUrl


class UrlSeri(ModelSerializer):

    org_url = serializers.URLField()  # Ensures valid URL input
    short_url = serializers.CharField(read_only=True)  # Prevents user input
    created_at = serializers.DateTimeField(read_only=True)  # Read-only field

    class Meta:
        model = ShortUrl
        fields = "__all__"
