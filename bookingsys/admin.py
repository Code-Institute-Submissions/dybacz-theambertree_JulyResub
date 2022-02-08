from django.contrib import admin
from . import models

admin.site.register(models.Table)
admin.site.register(models.BookingSlot)
admin.site.register(models.Booking)
admin.site.register(models.TimeSlot)
