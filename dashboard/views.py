from django import shortcuts
from django.views import generic, View
from . import models
from bookingsys import models
from django.http import HttpResponse, JsonResponse
import json
from django.core.serializers import serialize
from datetime import datetime, timedelta
# Create your views here.

current_date = datetime.now().date()


class DashboardHome(View):
    def get(self, request, *args, **kwargs):
        page_title = 'Home | Dashboard'
        page_type = 'dashboard'
        current_date = datetime.now().date()
        try:
            list_today_bookings = shortcuts.get_list_or_404(
                models.Booking.objects.filter(status=0))
            for i in list_today_bookings:
                time_slot = (i.timeslot.all())
                time_slot_date = (time_slot[0].date)
                if time_slot_date == current_date:
                    list_bookings.append(time_slot_date)
        except:
            list_today_bookings = 'No Data'

        list_bookings = []
        bookings_len = len(list_bookings)

        if request.user.is_staff:
            return shortcuts.render(
                request, "dashboard/home.html", {
                    'page_title': page_title,
                    'current_date': current_date,
                    'bookings_len': bookings_len,
                    'page_type': page_type,
                })
        else:
            return shortcuts.redirect("account_login")


class DashboardTables(View):
    """" """
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            data_from_post = json.load(request)['post_data']
            post_type = data_from_post[0]
            post_data = data_from_post[1]
            if post_type == 'add-form':
                models.Table.objects.create(
                    table_id=post_data[0],
                    table_capacity=post_data[1],
                )
                return HttpResponse(status=200)
            elif post_type == 'edit-form':
                table_pk = post_data[2]
                table = shortcuts.get_object_or_404(models.Table, pk=table_pk)
                table.table_id = post_data[0]
                table.table_capacity = post_data[1]
                table.save()

                return HttpResponse(status=200)
            elif post_type == 'non-form':
                tableId = kwargs['table_id']
                table = shortcuts.get_object_or_404(models.Table, pk=tableId)
                table.delete()
                return HttpResponse(status=200)
        else:
            return shortcuts.redirect("account_login")

    def get(self, request, *args, **kwargs):
        page_title = 'Tables | Dashboard'
        page_type = 'dashboard'

        table_objects = models.Table.objects.all()

        if request.user.is_staff:
            return shortcuts.render(
                request, "dashboard/tables.html", {
                    'page_title': page_title,
                    'page_type': page_type,
                    'current_date': current_date,
                    'tables': table_objects,
                })
        else:
            return shortcuts.redirect("account_login")


class DashboardTimes(View):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            data_from_post = json.load(request)['post_data']
            post_type = data_from_post[0]
            post_data = data_from_post[1]
            if post_type == 'add-form':
                time_str = post_data[0]
                time_format = '%H:%M'
                datetime_object = datetime.strptime(time_str, time_format)
                end_time = datetime_object + timedelta(minutes=90)
                models.TimeSlot.objects.create(
                    startTime=post_data[0],
                    endTime=end_time,
                )
                return HttpResponse(status=200)
            elif post_type == 'edit-form':
                table_pk = post_data[1]
                table = shortcuts.get_object_or_404(models.TimeSlot,
                                                    pk=table_pk)
                time_str = post_data[0]
                time_format = '%H:%M'
                datetime_object = datetime.strptime(time_str, time_format)
                end_time = datetime_object + timedelta(minutes=90)

                table.startTime = post_data[0]
                table.endTime = end_time
                table.save()

                return HttpResponse(status=200)
            elif post_type == 'non-form':
                timeslotId = kwargs['timeslot_id']
                timeslot = shortcuts.get_object_or_404(models.TimeSlot,
                                                       pk=timeslotId)
                timeslot.delete()
                return HttpResponse(status=200)
        else:
            return shortcuts.redirect("account_login")

    def get(self, request, *args, **kwargs):
        page_title = 'Times | Dashboard'
        page_type = 'dashboard'
        timeslot_objects = models.TimeSlot.objects.all()

        if request.user.is_staff:
            return shortcuts.render(
                request, "dashboard/times.html", {
                    'page_title': page_title,
                    'page_type': page_type,
                    'current_date': current_date,
                    'timeslots': timeslot_objects,
                })
        else:
            return shortcuts.redirect("account_login")


class DashboardSchedule(View):

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            data_from_post = json.load(request)['post_data']
            post_type = data_from_post[0]
            post_data = data_from_post[1]

            if post_type == 'add-form':
                table = shortcuts.get_object_or_404(models.Table, pk=post_data[1])
                timeslot = shortcuts.get_object_or_404(models.TimeSlot, pk=post_data[2])
                models.BookingSlot.objects.create(
                    date=post_data[0],
                    table=table,
                    time_slot=timeslot,
                    status=post_data[3],
                    booking_status=post_data[4],
                )
                return HttpResponse(status=200)
            elif post_type == 'edit-form':
                booking_slot_pk = post_data[5]
                booking_slot = shortcuts.get_object_or_404(models.BookingSlot, pk=booking_slot_pk)
                timeslot = shortcuts.get_object_or_404(models.TimeSlot, pk=post_data[2])
                table = shortcuts.get_object_or_404(models.Table, pk=post_data[1])
                booking_slot.table = table
                booking_slot.date = post_data[0]
                booking_slot.time_slot = timeslot
                booking_slot.status = post_data[3]
                booking_slot.booking_status = post_data[4]
                booking_slot.save()

                return HttpResponse(status=200)
            elif post_type == 'non-form':
                bookingSlotId = kwargs['bookingslot_id']
                print('message', bookingSlotId)
                bookingSlot = shortcuts.get_object_or_404(models.BookingSlot, pk=bookingSlotId)
                bookingSlot.delete()
                return HttpResponse(status=200)
        else:
            return shortcuts.redirect("account_login")

    def get(self, request, *args, **kwargs):
        page_title = 'Schedule | Dashboard'
        page_type = 'dashboard'

        schedule_objects = models.BookingSlot.objects.all()
        tables = serialize('json', models.Table.objects.all())
        times = serialize('json', models.TimeSlot.objects.all())


        if request.user.is_staff:
            return shortcuts.render(
                request, "dashboard/schedule.html", {
                    'page_title': page_title,
                    'page_type': page_type,
                    'current_date': current_date,
                    'bookingslots': schedule_objects,
                    'tables': tables,
                    'times': times,
                })
        else:
            return shortcuts.redirect("account_login")


class DashboardBookings(View):

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            data_from_post = json.load(request)['post_data']
            post_type = data_from_post[0]
            post_data = data_from_post[1]

            if post_type == 'add-form':
                booking_slot = shortcuts.get_object_or_404(models.BookingSlot, pk=post_data[3])
                booking = models.Booking.objects.create(
                    first_name=post_data[0],
                    last_name=post_data[1],
                    email=post_data[2],
                )
                booking.timeslot.add(booking_slot)
                booking_slot.booking_status = 0
                booking_slot.save()
                return HttpResponse(status=200)
            # elif post_type == 'edit-form':
            #     booking_slot_pk = post_data[5]
            #     booking_slot = shortcuts.get_object_or_404(models.BookingSlot, pk=booking_slot_pk)
            #     timeslot = shortcuts.get_object_or_404(models.TimeSlot, pk=post_data[2])
            #     table = shortcuts.get_object_or_404(models.Table, pk=post_data[1])
            #     booking_slot.table = table
            #     booking_slot.date = post_data[0]
            #     booking_slot.time_slot = timeslot
            #     booking_slot.status = post_data[3]
            #     booking_slot.booking_status = post_data[4]
            #     booking_slot.save()

            #     return HttpResponse(status=200)
            if post_type == 'non-form':
                bookingId = kwargs['booking_id']
                print('message', bookingId)
                booking = shortcuts.get_object_or_404(models.Booking, pk=bookingId)
                booking.status = 1
                booking.save()
                return HttpResponse(status=200)
        else:
            return shortcuts.redirect("account_login")

    def get(self, request, *args, **kwargs):
        page_title = 'Bookings | Dashboard'
        page_type = 'dashboard'

        booking_objects = models.Booking.objects.all()
        times = serialize('json', models.TimeSlot.objects.all())

        if request.user.is_staff:
            return shortcuts.render(
                request, "dashboard/bookings.html", {
                    'page_title': page_title,
                    'page_type': page_type,
                    'current_date': current_date,
                    'bookings': booking_objects,
                    'times': times,
                })
        else:
            return shortcuts.redirect("account_login")


class DashboardMenu(View):
    def get(self, request, *args, **kwargs):
        page_title = 'Menu | Dashboard'
        page_type = 'dashboard'

        if request.user.is_staff:
            return shortcuts.render(
                request, "dashboard/menu.html", {
                    'page_title': page_title,
                    'page_type': page_type,
                    'current_date': current_date,
                })
        else:
            return shortcuts.redirect("account_login")


class DashboardMessages(View):
    def get(self, request, *args, **kwargs):
        page_title = 'Messages | Dashboard'
        page_type = 'dashboard'

        if request.user.is_staff:
            return shortcuts.render(
                request, "dashboard/messages.html", {
                    'page_title': page_title,
                    'page_type': page_type,
                    'current_date': current_date,
                })
        else:
            return shortcuts.redirect("account_login")


class DashboardHelp(View):
    def get(self, request, *args, **kwargs):
        page_title = 'Help | Dashboard'
        page_type = 'dashboard'

        if request.user.is_staff:
            return shortcuts.render(
                request, "dashboard/help.html", {
                    'page_title': page_title,
                    'page_type': page_type,
                    'current_date': current_date,
                })
        else:
            return shortcuts.redirect("account_login")
