from . import models
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = models.Booking
        fields = (
            'number_of_guests',
            'timeslot',
            'comments',)
        labels = {
            'comments': ('Additional Information'),
        }
        widgets = {
            'timeslot': forms.CheckboxSelectMultiple(),
        }
