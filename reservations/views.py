from django.shortcuts import render, redirect, get_object_or_404
from reservations.models import *
from reservations.forms import *
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

	return render(request, 'create.html', args)


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

	return render(request, 'edit.html', args)


def delete(request, reservationId):
	# Assuming that delete confirmation will be displayed by the calling page
	reservation = get_object_or_404(Reservation, id=reservationId).delete()
	return redirect('/')


def hello(request, id = None): # For URL testing
	return HttpResponse("Hello, world.")


def customer_list(request):
	customers = Customer.objects.all()
	return render(request, 'customer_list.html', {
		'customers': customers
	})


def customer_delete(request, id):
	customer = get_object_or_404(Customer, id=id)
	customer.delete()
	return redirect('customer_list')


# HOW TO DO POST & GET
# https://docs.djangoproject.com/en/dev/topics/forms/#the-view
def customer_edit(request, id):
	customer = get_object_or_404(Customer, id=id)

	if request.method == 'POST':
		form = CustomerForm(request.POST, instance=customer)

		if form.is_valid():
			form.save()
			return redirect('customer_list')

	else:
		form = CustomerForm(instance=customer)

	return render(request, 'customer_edit.html', {
		'customer': customer,
		'form': form
		})

