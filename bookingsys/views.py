# from django.shortcuts import render, get_list_or_404, redirect,
#  get_object_or_404
from django import shortcuts
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
        timeslots = shortcuts.get_list_or_404(
            models.TimeSlot.objects.filter(status=1)
            )
        bookingslots = shortcuts.get_list_or_404(
            models.BookingSlot.objects.filter(status=1, booking_status=1)
            )
        page_type = 'bookingform'
        return shortcuts.render(
            request,
            "bookings.html",
            {
                # 'booking_form': BookingForm(),
                'timeslots': timeslots,
                'bookingslots': bookingslots,
                'page_type': page_type,
            }
        )

    def post(self, request, *args, **kwargs):
        booking_id = 1
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        number_of_guests = request.POST.get('guestnumber')
        comments = request.POST.get('comments')
        # bookingslotid = 'bookingslot' in request.POST
        idd = request.POST.get('bookingslot')
        print(idd)
        p1 = shortcuts.get_object_or_404(models.BookingSlot, id=idd)
        a1 = models.Booking.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            # account = ,
            number_of_guests=number_of_guests,
            status=0,
            comments=comments,
        )
        # a1
        # need a to check to see if booking has already been made then if so need to re render page with an error message.
        a1.timeslot.add(p1)
        # p1.booking_status(
        #     booking_status=booked,
        # )
        print(p1.booking_status)
        p1.booking_status = 0
        print(p1.booking_status)
        p1.save()
        return shortcuts.redirect('index')

    # def get(self, request, *args, **kwargs):

    #     return render(
    #         request,
    #         "bookings.html",
    #         {
    #             "booking_form": BookingForm()
    #         }
    #     )
