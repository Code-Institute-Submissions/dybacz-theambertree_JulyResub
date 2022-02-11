from django.shortcuts import render, get_list_or_404
from django.views import generic, View
from . import models
# from .forms import BookingForm


class BookingSlotList(generic.ListView):
    model = models.BookingSlot
    queryset = models.BookingSlot.objects.filter(status=1).order_by('-date')
    template_name = 'bookings.html'
    paginate_by = 6


class BookingSlot(View):

    def get(self, request, *args, **kwargs):
        timeslots = get_list_or_404(models.TimeSlot)
        bookingslots = get_list_or_404(models.BookingSlot)

        return render(
            request,
            "bookings.html",
            {
                # 'booking_form': BookingForm(),
                'timeslots': timeslots,
                'bookingslots': bookingslots
            }
        )

    # def get(self, request, *args, **kwargs):

    #     return render(
    #         request,
    #         "bookings.html",
    #         {
    #             "booking_form": BookingForm()
    #         }
    #     )
