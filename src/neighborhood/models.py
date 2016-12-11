from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.
class Neighborhood(models.Model):
    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)

    class Meta:
        ordering = ['-id']

class NeighborhoodMessage(models.Model):
    update_date = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    neighborhood = models.OneToOneField(Neighborhood)
