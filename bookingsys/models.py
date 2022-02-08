from django.db import models
from django.contrib.auth.models import User

A_STATUS = ((0, "Draft"), (1, "Published"))
B_STATUS = ((0, "Booked"), (1, "Availble"))
C_STATUS = ((0, "Booked"), (1, "Cancelled"))
D_STATUS = ((0, "Closed"), (1, "Open"))


class Table(models.Model):
    ''' Model for tables at restaurant'''
    table_name = models.CharField(max_length=15, unique=True)
    table_capacity = models.IntegerField(default=0)

    class Meta:
        ''' Method for ordering data '''
        ordering = ['-table_name']

    def __str__(self):
        return f"| Table: {self.table_name} | Capacity: {self.table_capacity}"


class TimeSlot(models.Model):
    ''' Model for Timeslots '''
    startTime = models.TimeField(unique=True)
    endTime = models.TimeField(unique=True)
    closed = models.IntegerField(choices=D_STATUS, default=0)

    class Meta:
        ''' Method for ordering data '''
        ordering = ['-startTime']

    def __str__(self):
        return f"Reservation: {self.startTime} - {self.endTime}"


class BookingSlot (models.Model):
    '''Model for empty bookable slots '''
    table = models.ForeignKey(
        Table,
        on_delete=models.CASCADE,
        related_name="timeslot",
        blank=True,
        null=True)
    date = models.DateField(blank=True, null=True)
    timeSlot = models.ForeignKey(
        TimeSlot,
        on_delete=models.CASCADE,
        related_name="bookingslot",
        blank=True,
        null=True)
    status = models.IntegerField(choices=A_STATUS, default=0)
    booking_status = models.IntegerField(choices=B_STATUS, default=1)

    class Meta:
        ''' Method for ordering data '''
        ordering = ['-date']

    def __str__(self):
        return f"{self.date} {self.timeSlot} {self.table}"


class Booking(models.Model):
    '''  Model for Active Bookings '''
    booking_id = models.IntegerField()
    guest = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="booking",
        blank=True,
        null=True)
    update_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=C_STATUS, default=0)
    comments = models.CharField(max_length=200)
    timeslot = models.ManyToManyField(
        BookingSlot,
        related_name="booking_table_slot",
        limit_choices_to={
            'status': 1,
            'booking_status': 1},
        blank=True)

    class Meta:
        ''' Method for ordering data '''
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.booking_id}"
