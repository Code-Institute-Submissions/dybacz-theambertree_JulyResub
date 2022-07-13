from django import shortcuts
from django.views import generic, View
from menu import models


class Index(View):
    def get(self, request, *args, **kwargs):
        page_type = 'home'
        page_title = 'The Amber Tree | Restaurant & Bar'
        try:
            menu = models.Item.objects.all()
        except:
            return print('No Menu Data')
        return shortcuts.render(
            request,
            "index.html",
            {
                # 'booking_form': BookingForm(),
                'page_type': page_type,
                'page_title': page_title,
                'menu': menu,
            })
