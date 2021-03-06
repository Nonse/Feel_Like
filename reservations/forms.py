from django import forms
from reservations.models import *


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
# To limit the set of displayed fields use:
# exclude = ['start_time', 'end_time']
# (or list the needed ones with "fields = ")
## To hide certain fields, we use widgets:
## https://docs.djangoproject.com/en/dev/topics/forms/modelforms/#overriding-the-default-fields
## with the hidden input class:
## https://docs.djangoproject.com/en/dev/ref/forms/widgets/#hiddeninput


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer


CUSTOMER_FIELDS = (
    'first_name',
    'last_name',
    'email',
    'street_address',
    'postcode',
    'city',
    'phone',
    'discount'
)


class ReservationCustomerForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=254)
    street_address = forms.CharField(max_length=200)
    postcode = forms.CharField(max_length=5)
    city = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100, required=False)
    discount = forms.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        model = Reservation
        fields = (
            'start_time',
            'end_time',
            'customer') + CUSTOMER_FIELDS + (
            'coach',
            'product',
            'location',
            'location_price',
            'participants',
            'amount'
        )

    def __init__(self, data=None, *args, **kwargs):
        super(ReservationCustomerForm, self).__init__(
            data=data, *args, **kwargs
        )
        if data and data.get('customer'):
            for field in CUSTOMER_FIELDS:
                self.fields[field].required = False

    def full_clean(self):
        if self.data and not self.data.get('customer'):
            customer_data = {}
            for field in CUSTOMER_FIELDS:
                customer_data[field] = self.data[field]
            form = CustomerForm(customer_data)
            if form.is_valid():
                customer = form.save()
                self.data = self.data.dict()
                self.data['customer'] = customer.id
        return super(ReservationCustomerForm, self).full_clean()


class CoachForm(forms.ModelForm):
    class Meta:
        model = Coach


COACH_FIELDS = (
    'first_name',
    'last_name',
    'phone'
    
)


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company


COMPANY_FIELDS = (
    'name',
    'street_address',
    'postcode',
    'city',
    'contact_person',
    'phone',
    'business_id',
    'iban',
    'location_vat'
    
)


class InvoiceForm(forms.ModelForm):
    reservations = forms.ModelMultipleChoiceField(
        queryset=Reservation.objects.filter(invoice__isnull=True)
    )

    class Meta:
        model = Invoice
        fields = (
            'date',
            'customer',
            'due_date',
            'reservations',
            'ref_number',
            'total'
        )
        widgets = {
            'ref_number': forms.TextInput(attrs={'readonly': True})
        }

    def __init__(self, data=None, *args, **kwargs):
        super(InvoiceForm, self).__init__(
            data=data, *args, **kwargs
        )

        if data and data.get('customer'):
            self.fields['reservations'].queryset = (
                self.fields['reservations'].queryset.filter(
                    customer_id=data.get('customer')
                )
            )

