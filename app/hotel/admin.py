from django.contrib import admin

from hotel.domain.final_client import FinalClient
from hotel.domain.hotel import Hotel
from hotel.domain.final_client_hotel import FinalClientHotel


class HotelAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'city',
        'id',
    ]


class FinalClientAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'id',
    ]

class FinalClientHotelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'check_in',
        'check_out',
        'hotel',
        'final_client',
    ]

admin.site.register(FinalClient, FinalClientAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(FinalClientHotel, FinalClientHotelAdmin)

