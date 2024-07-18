from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta

from apps.booking.validators import phone_validate


class Booking(models.Model):
    class Weekdays(models.IntegerChoices):
        MO = 0, 'Monday'
        TU = 1, 'Tuesday'
        WE = 2, 'Wednesday'
        TH = 3, 'Thursday'
        FR = 4, 'Friday'
        SA = 5, 'Saturday'
        SU = 6, 'Sunday'

    washing_type = models.ForeignKey('WashingType', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, validators=[phone_validate])

    arrival_time = models.TimeField()
    week_days = models.PositiveSmallIntegerField(choices=Weekdays.choices)

    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        arrival_datetime = datetime.combine(datetime.today(), self.arrival_time)
        end_time = arrival_datetime + timedelta(minutes=self.washing_type.time)

        objs = Booking.objects.filter(
            week_days=self.week_days,
            washing_type=self.washing_type,
            arrival_time__range=(self.arrival_time, end_time.time())
        )

        if objs.count() >= self.washing_type.number_of_places:
            raise ValidationError("This time is already booked")

    def __str__(self):
        return f"Booking on {self.get_week_days_display()} at {self.arrival_time}"


class WashingType(models.Model):
    name = models.CharField(max_length=100)
    time = models.PositiveSmallIntegerField(help_text='enter per minute')
    number_of_places = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name