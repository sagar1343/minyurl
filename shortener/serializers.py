from rest_framework import serializers
from .models import Link


class CreateLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ["url"]


class LinkSerializer(serializers.ModelSerializer):
    url = serializers.URLField(read_only=True)
    shortcode = serializers.CharField(read_only=True)
    clicks = serializers.IntegerField(read_only=True)

    class Meta:
        model = Link
        fields = [
            "id",
            "url",
            "shortcode",
            "is_active",
            "clicks",
            "expires_at",
            "created_at",
        ]
