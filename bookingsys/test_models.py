from django.test import TestCase
from .models import Table, TimeSlot, BookingSlot, Booking
from datetime import date


class TestModels(TestCase):

    def setUp(self):

        self.table = Table.objects.create(
            table_id=1,
            table_capacity=4
            )
        self.timeslot = TimeSlot.objects.create(
            startTime='18:00',
            endTime='19:30'
            )
        self.bookingslot = BookingSlot.objects.create(
            table=self.table,
            date=date.today(),
            time_slot=self.timeslot
            )
        self.booking = Booking.objects.create(
            first_name='John',
            last_name='Smith',
            email='john@smith.com',
        )
        self.booking.timeslot.add(self.bookingslot)

    def test_timeslot_defaults_to_status_closed(self):
        self.assertTrue(self.timeslot.status == 0)

    def test_bookingslot_defaults_to_status_draft(self):
        self.assertTrue(self.bookingslot.status == 0)

    def test_bookingslot_defaults_to_booking_status_available(self):
        self.assertTrue(self.bookingslot.booking_status == 1)

    def test_booking_defaults_to_status_booked(self):
        self.assertTrue(self.booking.status == 0)
