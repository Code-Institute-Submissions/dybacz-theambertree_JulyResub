from django.contrib import admin
from . import models


@admin.register(models.Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_id', 'table_capacity')
    search_fields = ['table_id', 'table_capacity']
    list_filter = ('table_capacity',)


@admin.register(models.BookingSlot)
class BookingSlotAdmin(admin.ModelAdmin):
    list_display = (
        # 'table_number',
        # 'table_capacity',
        'table',
        'date',
        'time_slot',
        'status',
        'booking_status')
    search_fields = ['table', 'date', 'time_slot', 'status', 'booking_status']
    list_filter = ('date', 'status', 'booking_status')
    actions = ['open_booking_slots', 'close_booking_slots']

    def open_booking_slots(self, request, queryset):
        queryset.update(status=1)

    def close_booking_slots(self, request, queryset):
        queryset.update(status=0)


@admin.register(models.Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'booking_name',
        'number_of_guests',
        'booking_table',
        'total_capacity',
        'reservation_date',
        'reservation_time',
        'status',
        'date_created',
        'comments')
    search_fields = ()
    list_filter = ('status',)


@admin.register(models.TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('startTime', 'endTime', 'status')
    search_fields = ['startTime']
    list_filter = ('status',)
    actions = ['open_slots', 'close_slots']

    def open_slots(self, request, queryset):
        queryset.update(status=1)

    def close_slots(self, request, queryset):
        queryset.update(status=0)
