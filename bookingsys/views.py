from django.shortcuts import render, get_list_or_404, redirect
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
        timeslots = get_list_or_404(models.TimeSlot.objects.filter(status=1))
        bookingslots = get_list_or_404(
            models.BookingSlot.objects.filter(status=1))

        return render(
            request,
            "bookings.html",
            {
                # 'booking_form': BookingForm(),
                'timeslots': timeslots,
                'bookingslots': bookingslots
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
        p1 = models.BookingSlot.objects.get(id=idd)
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
        a1.timeslot.add(p1)
        # print(p1)
        return redirect('index')

    # def get(self, request, *args, **kwargs):

    #     return render(
    #         request,
    #         "bookings.html",
    #         {
    #             "booking_form": BookingForm()
    #         }
    #     )
