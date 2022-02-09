from django.contrib import admin
from . import models


@admin.register(models.Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_name', 'table_capacity')
    search_fields = ['table_name', 'table_capacity']
    list_filter = ('table_name', 'table_capacity')


@admin.register(models.BookingSlot)
class BookingSlotAdmin(admin.ModelAdmin):
    list_display = (
        'table_number',
        'table_capacity',
        'date',
        'time_slot',
        'status',
        'booking_status')
    search_fields = ['table', 'date', 'time_slot', 'status', 'booking_status']
    list_filter = ('date', 'status', 'booking_status')


@admin.register(models.Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'booking_id',
        'guest',
        'booking_table',
        'number_of_guests',
        'total_capacity',
        'reservation_date',
        'reservation_time',
        'status',
        'date_of_booking',
        'comments')
    search_fields = ()
    list_filter = ('status',)


@admin.register(models.TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('startTime', 'endTime', 'closed')
    search_fields = ['startTime']
    list_filter = ('closed',)
