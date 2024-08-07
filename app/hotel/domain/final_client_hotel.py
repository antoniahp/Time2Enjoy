from django.db import models
from uuid import uuid4

from hotel.domain.hotel import Hotel
from hotel.domain.final_client import FinalClient

class FinalClientHotel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    final_client = models.ForeignKey(FinalClient, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hotel.name