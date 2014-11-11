from django.shortcuts import render_to_response, redirect, get_object_or_404
from reservations.models import Reservation
from reservations.forms import ReservationForm
from django.http import HttpResponse
from django.core.context_processors import csrf

# Tutorial: https://www.youtube.com/watch?v=gQe_8Q4YUpg
# Another one with a slightly different approach: http://www.peachybits.com/2011/09/django-1-3-form-api-modelform-example/

# Redirect to home page instead of 404 if reservation not found?

def create(request):
	if request.POST:
		form = ReservationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = ReservationForm()

	args = {}
	args.update(csrf(request))
	args['form'] = form

	return render_to_response('create.html', args)

def edit(request, reservationId):
	oldReservation = get_object_or_404(Reservation, id=reservationId)
	editResult = ''

	if request.POST:
		form = ReservationForm(request.POST, instance=oldReservation)
		if form.is_valid():
			form.save()
			editResult = "Changes saved"
	else:
		form = ReservationForm(instance=oldReservation)

	args = {}
	args.update(csrf(request))
	args['form'] = form
	args['editResult'] = editResult

	return render_to_response('edit.html', args)

def delete(request, reservationId):
	# Assuming that delete confirmation will be displayed by the calling page
	reservation = get_object_or_404(Reservation, id=reservationId).delete()
	return redirect('/')

def hello(request, id = None): # For URL testing
	return HttpResponse("Hello, world.")