# from django.db import models

# class Business(models.Model):
#     name = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name
    

from django.contrib.gis.db import models as gis_models
from django.db import models
import uuid


class Business(models.Model):
    # business_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255, db_index=True)

    category = models.CharField(max_length=100, db_index=True)
    sub_category = models.CharField(max_length=100, db_index=True)

    tags = models.JSONField(default=list, blank=True)

    # lat + long
    location = gis_models.PointField(geography=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# class Business(models.Model):
#     name = models.CharField(max_length=255, null=True, blank=True)

#     category = models.CharField(max_length=100, null=True, blank=True)
#     sub_category = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name
