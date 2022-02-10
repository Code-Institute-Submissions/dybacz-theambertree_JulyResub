from . import views
from django.urls import path


urlpatterns = [
    path('', views.BookingSlotList.as_view(), name='bookings_home')
]
