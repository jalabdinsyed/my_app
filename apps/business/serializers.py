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
    def create(self, validated_data):
        # 🔴 IMPORTANT: POP location FIRST
        location_data = validated_data.pop("location", None)

        # Create instance WITHOUT location
        instance = Business.objects.create(**validated_data)

        # Now safely set PointField
        if location_data:
            try:
                lng, lat = location_data["coordinates"]
                instance.location = Point(float(lng), float(lat))
                instance.save()
            except Exception:
                raise serializers.ValidationError(
                    {"location": "Invalid GeoJSON Point format"}
                )

        return instance