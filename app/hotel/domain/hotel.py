from django.db import models
from uuid import uuid4


class Hotel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    city = models.CharField(max_length=120)

    def __str__(self):
        return self.name