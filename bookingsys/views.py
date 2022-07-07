# from django.shortcuts import render, get_list_or_404, redirect,
#  get_object_or_404
from django import shortcuts
from django.views import generic, View
from . import models
from django.http import JsonResponse
import json
from django.core.serializers import serialize
# from .forms import BookingForm


class BookingSlotList(generic.ListView):
    model = models.BookingSlot
    queryset = models.BookingSlot.objects.filter(status=1).order_by('-date')
    template_name = 'bookings.html'
    paginate_by = 6


class AjaxRequest(generic.ListView):

    def post(self, request, *args, **kwargs):
        data = kwargs
        data_from_post = json.load(request)['post_data']
        print(data_from_post)
        try:
            bookingSlots = shortcuts.get_list_or_404(models.BookingSlot.objects.filter(date=data_from_post, booking_status=1))
            tablesOne = shortcuts.get_list_or_404(models.Table.objects)
        except Exception:
            return JsonResponse({'nodata': 'No dates Found'})

        print(bookingSlots, type(bookingSlots))
        new_list = json.loads(serialize('json', bookingSlots))
        table_list = json.loads(serialize('json', tablesOne))
        print(new_list, type(new_list))
        return JsonResponse({
            'data': new_list,
            'tables': table_list,
            })

class BookingSlot(View):

    def get(self, request, *args, **kwargs):
        timeslots = shortcuts.get_list_or_404(
            models.TimeSlot.objects
            )
        bookingslots = shortcuts.get_list_or_404(
            models.Table.objects
            )
        page_type = 'bookingform'
        page_title = 'Make a Booking | The Amber Tree'

        if request.user.is_authenticated:
            return shortcuts.render(
                request,
                "bookingsys/bookings.html",
                {
                    # 'booking_form': BookingForm(),
                    'timeslots': timeslots,
                    'bookingslots': bookingslots,
                    'page_type': page_type,
                    'page_title': page_title,
                }
            )
        else:
            return shortcuts.redirect("account_login")


    def post(self, request, *args, **kwargs):
        booking_id = 1
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
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
            status=0,
            comments=comments,
        )
        # a1
        # need a to check to see if booking has already been made then if so
        # need to re render page with an error message.
        a1.timeslot.add(p1)
        # p1.booking_status(
        #     booking_status=booked,
        # )
        print(p1.booking_status)
        p1.booking_status = 0
        print(p1.booking_status)
        p1.save()
        return shortcuts.render(
                request,
                "bookingsys/success.html"
            )