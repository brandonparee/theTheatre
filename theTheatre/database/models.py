from django.db import models

# Create your models here.
class Performance(models.Model):
	event = models.CharField(max_length=200)
	place = models.CharField(max_length=200)
	location = models.CharField(max_length=200)
	start_date = models.DateTimeField('date published')

	def __str__(self):
		return self.event


class Merchandise(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	price = models.DecimalField(max_digits = 5, decimal_places = 2)

class TicketSale(models.Model):
	place = models.CharField(max_length=200)
	location = models.CharField(max_length=200)
	start_date = models.DateTimeField('date published')
	price = models.DecimalField(max_digits = 5, decimal_places = 2)

#how to see whats in the database through CMD:
#CMD: python manage.py dumpdata <appname> <options>
#	python manage.py dumpdata database
#
#how to clear data from tables
#CMD: python manage.py flush
#
#how to load data into tables provided by the fixtures file (the default data that should belong in the database)
#CMD: python manage.py loaddata database_data.json
#
#What to edit what populates the tables when performing loaddata
#edit the fixtures file located at .\theTheatre\theTheatre\database\fixtures\database_test.json