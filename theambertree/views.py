from django import shortcuts
from django.views import generic, View
from menu import models
from django.http import HttpResponse


class Index(View):
    def get(self, request, *args, **kwargs):
        page_type = 'home'
        page_title = 'The Amber Tree | Restaurant & Bar'
        menu = models.Item.objects.all()
        return shortcuts.render(
                request,
                "index.html",
                {
                    'page_type': page_type,
                    'page_title': page_title,
                    'menu': menu,
                })
