# from django.db import models

# class Business(models.Model):
#     name = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name
    

from django.contrib.gis.db import models as gis_models
from django.db import models
import uuid


# class Business(models.Model):
#     business_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
#     name = models.CharField(max_length=255)

#     category = models.CharField(max_length=100)
#     sub_category = models.CharField(max_length=100)

#     tags = models.JSONField(default=list)

#     # ONE field for lat + long
#     location = gis_models.PointField(geography=True)

#     def __str__(self):
#         return self.name

class Business(models.Model):
    name = models.CharField(max_length=255)

    category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)

    def __str__(self):
        return self.name
