from . import views
from django.urls import path


urlpatterns = [
    path('', views.BookingSlot.as_view(), name='bookings_home'),
    path('ajax/<data_request>/', views.AjaxRequest.as_view(), name='ajax_request')
]
