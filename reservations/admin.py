from django.contrib import admin
from reservations.models import *

admin.site.register(Company)
admin.site.register(Coach)
admin.site.register(Product)
admin.site.register(Invoice)
admin.site.register(Reservation) #useful for invoice testing

# Register your models here.
