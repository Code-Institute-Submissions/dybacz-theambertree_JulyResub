from django import shortcuts
from django.views import generic, View
from . import models
from bookingsys import models
from django.http import HttpResponse, JsonResponse
import json
from django.core.serializers import serialize
from datetime import datetime
# Create your views here.


class Dashboard(View):

    def get(self, request, *args, **kwargs):
        page_title = 'Dashboard | The Amber Tree'
        page_type = 'dashboard'
        current_date = datetime.now().date()
        print(current_date)
        listTodayBookings = shortcuts.get_list_or_404(models.Booking.objects.filter(status=0))
        print(listTodayBookings) 
        if request.user.is_staff:
            return shortcuts.render(
                request,
                "dashboard/dashboard.html",
                {
                    'page_title': page_title,
                    'page_type': page_type,
                    'current_date': current_date,
                }
            )
        else:
            return shortcuts.redirect("account_login")