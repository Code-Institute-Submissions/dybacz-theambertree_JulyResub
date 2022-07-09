from django import shortcuts
from django.views import generic, View
from . import models
from bookingsys import models
from django.http import HttpResponse, JsonResponse
import json
from django.core.serializers import serialize
from datetime import datetime
# Create your views here.


class DashboardHome(View):

    def get(self, request, *args, **kwargs):
        page_title = 'Home | Dashboard'
        page_type = 'dashboard'
        current_date = datetime.now().date()
        print(current_date)
        list_today_bookings = shortcuts.get_list_or_404(models.Booking.objects.filter(status=0))
        list_bookings = []
        for i in list_today_bookings:
            time_slot = (i.timeslot.all())
            time_slot_date = (time_slot[0].date)
            if time_slot_date == current_date:
                list_bookings.append(time_slot_date)
        bookings_len = len(list_bookings)




        print(list_bookings) 
        if request.user.is_staff:
            return shortcuts.render(
                request,
                "dashboard/home.html",
                {
                    'page_title': page_title,
                    'current_date': current_date,
                    'bookings_len': bookings_len,
                    'page_type': page_type,
                }
            )
        else:
            return shortcuts.redirect("account_login")

class DashboardTables(View):
    def get(self, request, *args, **kwargs):
        page_title = 'Tables | Dashboard'
        page_type = 'dashboard'

        if request.user.is_staff:
            return shortcuts.render(
                request,
                "dashboard/tables.html",
                {
                    'page_title': page_title,
                    'page_type': page_type,

                }
            )
        else:
            return shortcuts.redirect("account_login")

class DashboardTimes(View):
    def get(self, request, *args, **kwargs):
        page_title = 'Times | Dashboard'
        page_type = 'dashboard'

        if request.user.is_staff:
            return shortcuts.render(
                request,
                "dashboard/times.html",
                {
                    'page_title': page_title,
                    'page_type': page_type,
                }
            )
        else:
            return shortcuts.redirect("account_login")


class DashboardSchedule(View):
    def get(self, request, *args, **kwargs):
        page_title = 'Schedule | Dashboard'
        page_type = 'dashboard'

        if request.user.is_staff:
            return shortcuts.render(
                request,
                "dashboard/schedule.html",
                {
                    'page_title': page_title,
                    'page_type': page_type,
                }
            )
        else:
            return shortcuts.redirect("account_login")


class DashboardBookings(View):
    def get(self, request, *args, **kwargs):
        page_title = 'Bookings | Dashboard'
        page_type = 'dashboard'

        if request.user.is_staff:
            return shortcuts.render(
                request,
                "dashboard/bookings.html",
                {
                    'page_title': page_title,
                    'page_type': page_type,
                }
            )
        else:
            return shortcuts.redirect("account_login")


class DashboardMessages(View):
    def get(self, request, *args, **kwargs):
        page_title = 'Messages | Dashboard'
        page_type = 'dashboard'

        if request.user.is_staff:
            return shortcuts.render(
                request,
                "dashboard/messages.html",
                {
                    'page_title': page_title,
                    'page_type': page_type,
                }
            )
        else:
            return shortcuts.redirect("account_login")


class DashboardHelp(View):
    def get(self, request, *args, **kwargs):
        page_title = 'Help | Dashboard'
        page_type = 'dashboard'

        if request.user.is_staff:
            return shortcuts.render(
                request,
                "dashboard/help.html",
                {
                    'page_title': page_title,
                    'page_type': page_type,
                }
            )
        else:
            return shortcuts.redirect("account_login")
