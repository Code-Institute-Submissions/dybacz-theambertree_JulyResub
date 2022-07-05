from django import shortcuts
from django.views import generic, View
from menu import models


# Class index(request):
#     return render(request, '../templates/index.html')

class Index(View):

    def get(self, request, *args, **kwargs):
        page_type = 'home'
        page_title = 'The Amber Tree | Restaurant & Bar'
        menu = shortcuts.get_list_or_404(
            models.Item
            )
        return shortcuts.render(
            request,
            "index.html",
            {
                # 'booking_form': BookingForm(),
                'page_type': page_type,
                'page_title': page_title,
                'menu': menu,
            }
        )
