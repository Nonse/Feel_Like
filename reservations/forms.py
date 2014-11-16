from django import forms
from reservations.models import *


class ReservationForm(forms.ModelForm):
	class Meta:
		model = Reservation
		# To limit the set of displayed fields use:
		# exclude = ['start_time', 'end_time']
		# (or list the needed ones with "fields = ")


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
    
