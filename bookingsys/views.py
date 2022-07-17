from django import shortcuts
from django.views import generic, View
from . import models
from django.http import JsonResponse, HttpResponse
import json
from django.core.serializers import serialize


class BookingSlotList(generic.ListView):
    model = models.BookingSlot
    queryset = models.BookingSlot.objects.filter(status=1).order_by('-date')
    template_name = 'bookings.html'
    paginate_by = 6


class AjaxRequest(generic.ListView):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            data = kwargs
            data_from_post = json.load(request)['post_data']
            try:
                bookingSlots = shortcuts.get_list_or_404(
                    models.BookingSlot.objects.filter(date=data_from_post,
                                                      booking_status=1))
                tablesOne = shortcuts.get_list_or_404(models.Table.objects)
            except Exception:
                return JsonResponse({'nodata': 'No dates Found'})

            new_list = json.loads(serialize('json', bookingSlots))
            table_list = json.loads(serialize('json', tablesOne))
            return JsonResponse({
                'data': new_list,
                'tables': table_list,
            })
        else:
            return shortcuts.redirect("account_login")


class BookingSlot(View):
    def get(self, request, *args, **kwargs):
        timeslots = models.TimeSlot.objects.all()
        bookingslots = models.Table.objects.all()
        page_type = 'bookingform'
        page_title = 'Make a Booking | The Amber Tree'

        if request.user.is_authenticated:
            return shortcuts.render(
                request, "bookingsys/bookings.html", {
                    'timeslots': timeslots,
                    'bookingslots': bookingslots,
                    'page_type': page_type,
                    'page_title': page_title,
                })
        else:
            return shortcuts.redirect("account_login")

    def post(self, request, *args, **kwargs):
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        comments = request.POST.get('comments')
        idd = request.POST.get('bookingslot')
        user = request.user
        bookingSlot = shortcuts.get_object_or_404(models.BookingSlot, id=idd)
        bookingObj = models.Booking.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            account=user,
            status=0,
            comments=comments,
        )
        # a1
        # need a to check to see if booking has already been made then if so
        # need to re render page with an error message.
        bookingObj.timeslot.add(bookingSlot)
        # p1.booking_status(
        #     booking_status=booked,
        # )
        bookingSlot.booking_status = 0
        bookingSlot.save()
        return shortcuts.render(request, "bookingsys/success.html")


class Bookings(View):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            bookingId = kwargs['booking_id']
            booking = shortcuts.get_object_or_404(models.Booking, pk=bookingId)
            booking.status = 1
            booking.save()
            bookingSlotId = booking.timeslot.all()[0].pk
            bookingSlot = shortcuts.get_object_or_404(models.BookingSlot,
                                                      pk=bookingSlotId)
            bookingSlot.booking_status = 1
            bookingSlot.save()
            return HttpResponse(status=200)
        else:
            return shortcuts.redirect("account_login")

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user
            bookings = models.Booking.objects.filter(
                timeslot__isnull=False, account=user,
                status=0).order_by('timeslot')
            return shortcuts.render(request, "bookingsys/my_bookings.html", {
                'bookings': bookings,
            })
        else:
            return shortcuts.redirect("account_login")
