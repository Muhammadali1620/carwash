from rest_framework import generics

from apps.booking.models import Booking, WashingType
from apps.booking.serializers import BookingSerializer, WashingTypeSerializer


class BookingCreateAPIView(generics.CreateAPIView):
    model = Booking
    serializer_class = BookingSerializer


class WashingTypeListAPIView(generics.ListAPIView):
    queryset = WashingType.objects.all()
    serializer_class = WashingTypeSerializer