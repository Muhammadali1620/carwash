from django.urls import path
from . import views


urlpatterns = [
    path('', views.BookingCreateAPIView.as_view(), name='booking_list'),
    path('washing_type/', views.WashingTypeListAPIView.as_view(), name='washing_type'),
]