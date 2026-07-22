from rest_framework import serializers
from .models import Link


class CreateLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ["url"]

    def create(self, validated_data):
        validated_data["owner"] = self.context.get("request").user
        return super().create(validated_data)


class LinkSerializer(serializers.ModelSerializer):
    url = serializers.URLField(read_only=True)
    short_code = serializers.CharField(read_only=True)
    clicks = serializers.IntegerField(read_only=True)

    class Meta:
        model = Link
        fields = [
            "id",
            "url",
            "short_code",
            "is_active",
            "clicks",
            "expires_at",
            "created_at",
        ]
