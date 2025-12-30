from rest_framework import serializers
from django.contrib.gis.geos import Point
from .models import Business

class BusinessSerializer(serializers.ModelSerializer):
    lat = serializers.FloatField(write_only=True)
    lng = serializers.FloatField(write_only=True)

    class Meta:
        model = Business
        fields = (
            "id",
            "name",
            "category",
            "sub_category",
            "tags",
            "lat",
            "lng",
            "location",
            "created_at",
        )
        read_only_fields = ("location", "created_at")

    def create(self, validated_data):
        lat = validated_data.pop("lat")
        lng = validated_data.pop("lng")
        validated_data["location"] = Point(lng, lat)
        return super().create(validated_data)
