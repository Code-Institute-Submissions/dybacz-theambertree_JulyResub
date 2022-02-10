from django.shortcuts import render
from django.views import generic
from . import models


class BookingSlotList(generic.ListView):
    model = models.BookingSlot
    queryset = models.BookingSlot.objects.filter(status=1).order_by('-date')
    template_name = 'bookings.html'
    paginate_by = 6
