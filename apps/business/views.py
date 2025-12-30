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
