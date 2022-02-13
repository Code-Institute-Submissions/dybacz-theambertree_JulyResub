from django import shortcuts
from django.views import generic, View


# Class index(request):
#     return render(request, '../templates/index.html')

class Index(View):

    def get(self, request, *args, **kwargs):
        page_type = 'home'
        return shortcuts.render(
            request,
            "index.html",
            {
                # 'booking_form': BookingForm(),
                'page_type': page_type,
            }
        )
