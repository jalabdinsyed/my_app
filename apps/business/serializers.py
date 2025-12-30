from rest_framework import serializers
from .models import Business

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        geo_field = "location"   # Important
        fields = (
            "id",
            "name",
            "category",
            "sub_category",
            "tags",
            "location",
            "created_at",
        )
