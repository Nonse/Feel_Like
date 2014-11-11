from django.db import models


class Reservation(models.Model):
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	customer = models.ForeignKey('Customer')
	coach = models.ForeignKey('Coach')
	product = models.ForeignKey('Product')
	location = models.CharField(max_length=200)
	location_price = models.DecimalField(max_digits=10, decimal_places=2)
	participants = models.IntegerField()
	amount = models.DecimalField(max_digits=10, decimal_places=2)

class Customer(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField(max_length=254)
	street_address = models.CharField(max_length=200)
	postcode = models.CharField(max_length=5) #Finnish postal code length
	city = models.CharField(max_length=100)
	phone = models.CharField(max_length=100, null=True, blank=True)
	discount = models.DecimalField(max_digits=5, decimal_places=2) #999,99 max
	def __str__(self):
		return '%s, %s' % (self.last_name, self.first_name)

class Coach(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)
	def __str__(self):
		return '%s, %s' % (self.last_name, self.first_name)

class Product(models.Model):
	name = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	vat = models.DecimalField(max_digits=10, decimal_places=2)
	def __str__(self):
		return '%s' % (self.name)

class Invoice(models.Model):
	date = models.DateField()
	reservation = models.OneToOneField('Reservation')
	company = models.ForeignKey('Company')

class Company(models.Model):
	name = models.CharField(max_length=100)
	street_address = models.CharField(max_length=200)
	postcode = models.CharField(max_length=5) #Finnish postal code length
	city = models.CharField(max_length=100)
	contact_person = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)
	business_id = models.CharField(max_length=100, null=True, blank=True)
	iban = models.CharField(max_length=100, null=True, blank=True)
	location_vat = models.DecimalField(max_digits=10, decimal_places=2)

