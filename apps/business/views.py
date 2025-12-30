from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

from .models import Business
from .serializers import BusinessSerializer


class BusinessViewSet(ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    permission_classes = [AllowAny]

    # 🔹 OVERRIDE CREATE (optional)
    def create(self, request, *args, **kwargs):
        print("Custom create logic")
        return super().create(request, *args, **kwargs)

    # 🔹 CUSTOM ACTION (DETAIL)
    @action(detail=True, methods=["post"])
    def activate(self, request, pk=None):
        """
        POST /business/{id}/activate/
        """
        business = self.get_object()
        business.is_active = True
        business.save()
        return Response({"status": "business activated"})

    # 🔹 CUSTOM ACTION (DETAIL)
    @action(detail=True, methods=["post"])
    def deactivate(self, request, pk=None):
        """
        POST /business/{id}/deactivate/
        """
        business = self.get_object()
        business.is_active = False
        business.save()
        return Response({"status": "business deactivated"})

    # 🔹 CUSTOM ACTION (LIST)
    @action(detail=False, methods=["get"])
    def active(self, request):
        """
        GET /business/active/
        """
        qs = self.get_queryset().filter(is_active=True)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)


    @action( detail=False, methods=["get"], url_path="search", url_name="search")
    def search_businesses(self, request):
        lat = request.query_params.get("lat")
        lng = request.query_params.get("lng")
        query = request.query_params.get("query")
        distance = request.query_params.get("distance", 5)
        unit = request.query_params.get("unit", "km")

        if not lat or not lng:
            return Response(
                {"error": "lat and lng are required"},
                status=400
            )

        user_location = Point(float(lng), float(lat), srid=4326)

        if unit == "m":
            dist = D(m=float(distance))
        else:
            dist = D(km=float(distance))

        qs = Business.objects.filter(
            location__distance_lte=(user_location, dist)
        )

        if query:
            qs = qs.filter(
                Q(category__icontains=query) |
                Q(sub_category__icontains=query) |
                Q(tags__icontains=query)
            )

        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)



    

# | Method | URL                              | Purpose     |
# | ------ | -------------------------------- | ----------- |
# | POST   | `/api/business/`                 | Create      |
# | GET    | `/api/business/`                 | List        |
# | GET    | `/api/business/{id}/`            | Retrieve    |
# | PUT    | `/api/business/{id}/`            | Update      |
# | DELETE | `/api/business/{id}/`            | Delete      |
# | POST   | `/api/business/{id}/activate/`   | Custom      |
# | POST   | `/api/business/{id}/deactivate/` | Custom      |
# | GET    | `/api/business/active/`          | Custom list |
