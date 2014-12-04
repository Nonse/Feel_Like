from django.shortcuts import render, redirect, get_object_or_404
from reservations.models import *
from reservations.forms import *
from django.http import HttpResponse
from django.core.context_processors import csrf
from dateutil import parser
from django.contrib.auth.decorators import login_required 

# Tutorial: https://www.youtube.com/watch?v=gQe_8Q4YUpg
# Another one with a slightly different approach: http://www.peachybits.com/2011/09/django-1-3-form-api-modelform-example/

# Redirect to home page instead of 404 if reservation not found?

class ReservationInvoice:
    def __init__(self, reservation, invoice):
        self.reservation = reservation
        self.invoice = invoice

@login_required(login_url='/login/')  
def list(request):
    reservations = Reservation.objects.all()
    invoices = Invoice.objects.all()

    res_inv = []
    
    for r in reservations:
        i = invoices.filter(reservation_id = r.id)
        if i.exists():
            res_inv.append(ReservationInvoice(r, i[0]))
        else:
            res_inv.append(ReservationInvoice(r, None))

    args = {}
    args['res_inv'] = res_inv
    return render(request, 'list.html', args)

@login_required(login_url='/login/')  
def create(request):
    if request.POST:
        form = ReservationCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.session['http_referer'])
    else:
        startTime, endTime = None, None
        
        startRequest = request.GET.get('startTime')
        endRequest = request.GET.get('endTime')

        # Requires python-dateutil!
        if (startRequest):
            startTime = parser.parse(startRequest)
        if (endRequest):
            endTime = parser.parse(endRequest)

        form = ReservationCustomerForm(initial = {'start_time': startTime, 'end_time': endTime})

        request.session['http_referer'] = request.META.get('HTTP_REFERER', '/')

    args = {}
    args.update(csrf(request))
    args['form'] = form

    return render(request, 'create.html', args)

@login_required(login_url='/login/')  
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
        request.session['http_referer'] = request.META.get('HTTP_REFERER', '/')

    args = {}
    args.update(csrf(request))
    args['form'] = form
    args['editResult'] = editResult

    return render(request, 'edit.html', args)

@login_required(login_url='/login/')  
def delete(request, reservationId):
    # Assuming that delete confirmation will be displayed by the calling page
    reservation = get_object_or_404(Reservation, id=reservationId).delete()
    return redirect(request.META.get('HTTP_REFERER'))


def hello(request, id = None): # For URL testing
    return HttpResponse("Hello, world.")

@login_required(login_url='/login/')  
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {
        'customers': customers
    })

@login_required(login_url='/login/')  
def customer_delete(request, id):
    customer = get_object_or_404(Customer, id=id)
    customer.delete()
    return redirect('customer_list')


# HOW TO DO POST & GET
# https://docs.djangoproject.com/en/dev/topics/forms/#the-view
@login_required(login_url='/login/')  
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

