from django.db import models

# Create your models here.
class Performance(models.Model):
	event = models.CharField(max_length=200)
	place = models.CharField(max_length=200)
	location = models.CharField(max_length=200)
	start_date = models.DateTimeField('date published')


class Merchandise(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	price = models.DecimalField(max_digits = 5, decimal_places = 2)

class TicketSale(models.Model):
	place = models.CharField(max_length=200)
	location = models.CharField(max_length=200)
	start_date = models.DateTimeField('date published')
	price = models.DecimalField(max_digits = 5, decimal_places = 2)
