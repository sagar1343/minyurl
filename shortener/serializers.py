from rest_framework import serializers
from .models import Link


class CreateLinkSerializer(serializers.ModelSerializer):
    class meta:
        model = Link
        fields = ["url"]


class LinkSerializer(serializers.ModelSerializer):
    class meta:
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
