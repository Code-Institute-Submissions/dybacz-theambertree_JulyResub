from django.test import TestCase
from django.contrib.auth.models import User
from .models import Booking, BookingSlot, Table, TimeSlot
from datetime import date
import json
from django.core.serializers import serialize


class TestViews(TestCase):
    """"""
    def test_get_my_bookings_page_as_guest(self):
        response = self.client.get('/bookings/my-bookings')
        self.assertEqual(response.status_code, 302)

    def test_get_my_bookings_page_as_guest_and_redirect(self):
        response = self.client.get('/bookings/my-bookings', follow=True)
        self.assertRedirects(response, '/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_get_my_bookings_page_as_user(self):
        user = User.objects.create_user(
            'testuser', 'testuser@test.com', 'testpassword')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get('/bookings/my-bookings')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookingsys/my_bookings.html')

    def test_get_booking_page_as_guest(self):
        response = self.client.get('/bookings/')
        self.assertEqual(response.status_code, 302)

    def test_get_booking_page_as_guest_and_redirect(self):
        response = self.client.get('/bookings/', follow=True)
        self.assertRedirects(response, '/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_get_booking_page_as_user(self):
        user = User.objects.create_user(
            'testuser', 'testuser@test.com', 'testpassword')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get('/bookings/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookingsys/bookings.html')

    def test_get_remove_booking_page_as_user(self):
        user = User.objects.create_user(
            'testuser', 'testuser@test.com', 'testpassword')
        booking = Booking.objects.create(
            first_name='John', last_name='Smith', account=user, status=0)
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(
            f'/bookings/my-bookings/remove/{booking.pk}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookingsys/my_bookings.html')

    def test_get_remove_booking_page_as_guest(self):
        booking = Booking.objects.create(
            first_name='John', last_name='Smith', status=0)
        response = self.client.get(
            f'/bookings/my-bookings/remove/{booking.pk}')
        self.assertEqual(response.status_code, 302)

    def test_get_remove_booking_page_as_guest_and_redirect(self):
        booking = Booking.objects.create(
            first_name='John', last_name='Smith', status=0)
        response = self.client.get(
            f'/bookings/my-bookings/remove/{booking.pk}', follow=True)
        self.assertRedirects(response, '/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_post_ajax_date_requests_as_user(self):
        user = User.objects.create_user(
            'testuser', 'testuser@test.com', 'testpassword')
        dataRequest = 'timeslots'
        data = date.today()
        table = Table.objects.create(table_id=1, table_capacity=2)
        time_slot = TimeSlot.objects.create(startTime='18:00', endTime='19:30')
        booking_slot = BookingSlot.objects.create(
            date=data, booking_status=1, time_slot=time_slot, table=table)
        booking_slot_list = json.loads(serialize(
            'json', BookingSlot.objects.filter(
                date=data, booking_status=1)))
        table_list = json.loads(serialize('json', Table.objects.all()))
        self.client.login(username='testuser', password='testpassword')
        json_data = {'post_data': data}
        response = self.client.post(
            f'/bookings/ajax/{dataRequest}/',
            content_type='application/json',
            data=json_data)
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'data': booking_slot_list, 'tables': table_list, })

    def test_post_my_bookings_page_as_user_delete_booking(self):
        user = User.objects.create_user(
            'testuser', 'testuser@test.com', 'testpassword')
        data = date.today()
        table = Table.objects.create(table_id=1, table_capacity=2)
        time_slot = TimeSlot.objects.create(startTime='18:00', endTime='19:30')
        booking_slot = BookingSlot.objects.create(
            date=data, booking_status=0, time_slot=time_slot, table=table)
        booking = Booking.objects.create(status=0)
        booking.timeslot.add(booking_slot)

        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(
            f'/bookings/my-bookings/remove/{booking.pk}')
        self.assertEqual(response.status_code, 200)
        # refresh dbs
        booking.refresh_from_db()
        booking_slot.refresh_from_db()
        # check that booking status of empty slot is now available
        self.assertEqual(booking_slot.booking_status, 1)
        # check that status of cancelled booking is now available
        self.assertEqual(booking.status, 1)

    def test_post_booking_page_create_booking(self):
        user = User.objects.create_user(
            'testuser', 'testuser@test.com', 'testpassword')
        data = date.today()
        table = Table.objects.create(table_id=1, table_capacity=2)
        time_slot = TimeSlot.objects.create(startTime='18:00', endTime='19:30')
        booking_slot = BookingSlot.objects.create(
            date=data, booking_status=1, time_slot=time_slot, table=table)
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post('/bookings/', {
            'firstname': 'John',
            'lastname': 'Smith',
            'email': 'john@smith.com',
            'bookingslot': booking_slot.pk,
            'comments': 'comment'})
        self.assertEqual(response.status_code, 200)

        # refresh db
        booking_slot.refresh_from_db()
        # check booking slot status has changed from avaialble to booked
        self.assertEqual(booking_slot.booking_status, 0)
        # find booking just created with matching booking slot
        booking = Booking.objects.filter(timeslot=booking_slot.pk)
        # check booking status is booked
        self.assertEqual(booking.all()[0].status, 0)
