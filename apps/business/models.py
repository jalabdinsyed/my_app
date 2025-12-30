from django.db import models
from django.contrib.gis.db import models as gis_models
from django.utils import timezone
import uuid


class Business(models.Model):
    name = models.CharField(max_length=255, db_index=True)

    category = models.CharField(max_length=100, db_index=True)
    sub_category = models.CharField(max_length=100, db_index=True)

    tags = models.JSONField(default=list, blank=True)

    # GIS field ONLY
    location = gis_models.PointField(null=True, blank=True)

    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
