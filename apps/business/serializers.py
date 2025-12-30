# from rest_framework import serializers
# from .models import Business

# class BusinessSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Business
#         geo_field = "location"   # Important
#         fields = (
#             "id",
#             "name",
#             "category",
#             "sub_category",
#             "tags",
#             "location",
#             "created_at",
#         )

from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import Business

class BusinessSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Business
        geo_field = "location"   # VERY IMPORTANT
        fields = (
            "id",
            "name",
            "category",
            "sub_category",
            "tags",
            "location",
            "created_at",
        )