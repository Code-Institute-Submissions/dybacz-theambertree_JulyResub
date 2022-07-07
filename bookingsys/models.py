from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
import datetime

A_STATUS = ((0, "Draft"), (1, "Published"))
B_STATUS = ((0, "Booked"), (1, "Availble"))
C_STATUS = ((0, "Booked"), (1, "Cancelled"), (2, "Attended"))
D_STATUS = ((0, "Closed"), (1, "Open"))


class Table(models.Model):
    ''' Model for tables at restaurant'''
    table_id = models.IntegerField(default=1)
    table_capacity = models.IntegerField(default=1)

    class Meta:
        ''' Method for ordering data '''
        ordering = ['-table_id']

    def __str__(self):
        return f"Table: {self.table_id} | Capacity: {self.table_capacity}"


class TimeSlot(models.Model):
    ''' Model for Timeslots '''
    startTime = models.TimeField()
    endTime = models.TimeField()
    status = models.IntegerField(choices=D_STATUS, default=0)

    class Meta:
        ''' Method for ordering data '''
        ordering = ['startTime']

    def __str__(self):
        return f"{self.startTime} - {self.endTime}"


class BookingSlot (models.Model):
    '''Model for empty bookable slots '''
    table = models.ForeignKey(
        Table,
        on_delete=models.CASCADE,
        related_name="timeslot",
        blank=True,
        null=True)
    date = models.DateField(blank=True, null=True)
    time_slot = models.ForeignKey(
        TimeSlot,
        on_delete=models.CASCADE,
        limit_choices_to={
            'status': 1},
        related_name="bookingslot", default='')
    status = models.IntegerField(choices=A_STATUS, default=0)
    booking_status = models.IntegerField(choices=B_STATUS, default=1)

    class Meta:
        ''' Method for ordering data '''
        ordering = ['-date']
        unique_together = [['table', 'date', 'time_slot']]

    def __str__(self):
        return f"{self.table} | {self.date} | {self.time_slot}"

    # @admin.display
    # def table_capacity(self):
    #     ''' Loop for displaying table capcity on admin booking slot panel '''
    #     capacity = 0
    #     # for i in self.time_slot.all():
    #     x_string = str(self.table).split("| ")
    #     z_string = x_string[1].split(" ")
    #     capacity += int(z_string[1])
    #     #     concat += x_list[1]
    #     return capacity

    # def table_number(self):
    #     ''' Loop for displaying table number on admin booking slot panel '''
    #     x_string = str(self.table).split(" ")
    #     return x_string[1]


class Booking(models.Model):
    '''  Model for Active Bookings '''
    booking_id = models.IntegerField(blank=True, default=0)
    first_name = models.CharField(max_length=15, default='first name')
    last_name = models.CharField(max_length=20, default='last name')
    email = models.EmailField(default='guest@email.com')
    account = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="booking",
        blank=True,
        null=True)
    update_on = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=C_STATUS, default=0)
    comments = models.CharField(max_length=200, blank=True)

    timeslot = models.ManyToManyField(
        BookingSlot,
        related_name="booking_table_slot",
        # limit_choices_to={
        #     'status': 1,
        #     'booking_status': 1,
        #     'date__range': (
        #         datetime.date.today(), datetime.date.today()+datetime.timedelta(days=30))
        #     },
        default='')

    class Meta:
        ''' Method for ordering data '''
        ordering = ['-date_created']

    def __str__(self):
        return f"{self.booking_id}"

    @admin.display
    def booking_name(self):
        '''Returns Fullname'''
        return f"{self.last_name}, {self.first_name}"

    def booking_table(self):
        ''' Loop for displaying table number on admin booking panel '''
        concat = []
        for i in self.timeslot.get_queryset():
            x_list = str(i).split("| ")
            concat.append(x_list[0])
        concat.reverse()
        return concat

    def total_capacity(self):
        '''Loop for displaying booking total capcity on admin booking panel
        '''
        concat = ""
        capacity = 0
        for i in self.timeslot.get_queryset():
            x_list = str(i).split("| ")
            z_list = x_list[1].split(" ")
            capacity += int(z_list[1])
            concat += x_list[1]
        return f"{capacity}"

    def reservation_date(self):
        ''' Loop for displaying reservation date on admin booking panel '''
        for i in self.timeslot.get_queryset():
            x_list = str(i).split("| ")
            return f"{x_list[2]}"

    def reservation_time(self):
        ''' Loop for displaying reservation time on admin booking panel '''
        for i in self.timeslot.get_queryset():
            x_list = str(i).split("| ")
            return f"{x_list[3]}"
