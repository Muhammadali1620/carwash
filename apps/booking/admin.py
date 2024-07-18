from django.contrib import admin

from apps.booking.models import Booking, WashingType


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone_number', 'arrival_time', 'week_days']
    list_display_links = list_display


@admin.register(WashingType)
class WashingTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'time', 'number_of_places', 'price']
    list_display_links = list_display