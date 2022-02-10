from django.shortcuts import render
from django.views import generic, View
from . import models
from .forms import BookingForm


class BookingSlotList(generic.ListView):
    model = models.BookingSlot
    queryset = models.BookingSlot.objects.filter(status=1).order_by('-date')
    template_name = 'bookings.html'
    paginate_by = 6


class BookingSlot(View):

    def get(self, request, *args, **kwargs):

        return render(
            request,
            "bookings.html",
            {
                "booking_form": BookingForm()
            }
        )
