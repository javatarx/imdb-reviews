import uuid

from django.db import models


class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    date = models.CharField(max_length=200, null=True, blank=True)
    url = models.TextField(null=True, blank=True)
    movie = models.TextField(null=True, blank=True)
    rating = models.CharField(max_length=10, null=True, blank=True)
    is_positive = models.BooleanField(null=True, blank=True)
