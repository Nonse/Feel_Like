from django.shortcuts import render, redirect, get_object_or_404
from reservations.models import *
from reservations.forms import *
from django.http import HttpResponse
from django.core.context_processors import csrf
from dateutil import parser
from django.contrib.auth.decorators import login_required 
from cal.views import timeIncrement
from datetime import date
from .utils import *

# Tutorial: https://www.youtube.com/watch?v=gQe_8Q4YUpg
# Another one with a slightly different approach: http://www.peachybits.com/2011/09/django-1-3-form-api-modelform-example/

# Redirect to home page instead of 404 if reservation not found?

@login_required()  
def list(request):
    reservations_all = Reservation.objects.all()
    reservations_invoiced = Reservation.objects.filter(invoice__isnull=False)
    reservations_not_invoiced = Reservation.objects.filter(invoice__isnull=True)

    return render(request, 'list.html', {
        'all': reservations_all,
        'invoiced': reservations_invoiced,
        'not_invoiced': reservations_not_invoiced
    })

@login_required()  
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
            endTime += timeIncrement # duration of one slot in the calendar

        form = ReservationCustomerForm(initial = {'start_time': startTime, 'end_time': endTime})

        request.session['http_referer'] = request.META.get('HTTP_REFERER', '/')

    args = {}
    args.update(csrf(request))
    args['form'] = form

    return render(request, 'create.html', args)

@login_required()  
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

@login_required()  
def delete(request, reservationId):
    # Assuming that delete confirmation will be displayed by the calling page
    reservation = get_object_or_404(Reservation, id=reservationId).delete()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required()  
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {
        'customers': customers
    })

@login_required()  
def customer_delete(request, id):
    customer = get_object_or_404(Customer, id=id)
    customer.delete()
    return redirect('customer_list')


# HOW TO DO POST & GET
# https://docs.djangoproject.com/en/dev/topics/forms/#the-view
@login_required()  
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


@login_required()  
def coach_list(request):
    coaches = Coach.objects.all()
    return render(request, 'coach_list.html', {
        'coaches': coaches
    })

@login_required()  
def coach_delete(request, id):
    coach = get_object_or_404(Coach, id=id)
    coach.delete()
    return redirect('coach_list')


@login_required()  
def coach_edit(request, id):
    coach = get_object_or_404(Coach, id=id)

    if request.method == 'POST':
        form = CoachForm(request.POST, instance=coach)

        if form.is_valid():
            form.save()
            return redirect('coach_list')

    else:
        form = CoachForm(instance=coach)

    return render(request, 'coach_edit.html', {
        'coach': coach,
        'form': form
        })

@login_required()  
def company_edit(request):
    company = get_object_or_404(Company, id=1)

    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
    else:
        form = CompanyForm(instance=company)

    return render(request, 'company_edit.html', {
        'company': company,
        'form': form
        })


@login_required()
def invoice_create(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save(commit=False) #to get object from form
            invoice.company = Company.objects.all()[0] #adding company info
            invoice.save() #saving modified invoice
            for r in form.cleaned_data['reservations']:#add invoice to r
                r.invoice = invoice
                r.save()
            return redirect('r_list')
    else:
        last_invoice = Invoice.objects.order_by('-id')[0:1]#1st element + cast to list
        if last_invoice:
            next_id = last_invoice[0].id + 1
        else:
            next_id = 1

        initial = {
            'date': date.today(),
            'customer': request.GET['customer'],
            'reservations': request.GET.getlist('reservations', []),
            'ref_number': make_referencenumber(str(next_id + 1000))
        }
        form = InvoiceForm(initial=initial)
    return render(request, 'invoice_create.html', {
        'form': form
    })

