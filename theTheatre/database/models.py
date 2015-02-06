from django.db import models

# Create your models here.
class Performance(models.Model):
	event = models.CharField(max_length=200)
	place = models.CharField(max_length=200)
	location = models.CharField(max_length=200)
	date = models.DateTimeField('date published')
	image = models.URLField(max_length=200)

	def __str__(self):
		return self.event


class Merchandise(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	price = models.DecimalField(max_digits = 5, decimal_places = 2)
	image = models.URLField(max_length=200)

class TicketSale(models.Model):
	place = models.CharField(max_length=200)
	location = models.CharField(max_length=200)
	date = models.DateTimeField('date published')
	price = models.DecimalField(max_digits = 5, decimal_places = 2)

#how to see whats in the database through CMD:
#CMD: python manage.py dumpdata <appname> <options>
#	python manage.py dumpdata database --indent 2
#
#how to clear data from tables
#CMD: python manage.py flush
#
#how to load data into tables provided by the fixtures file (the default data that should belong in the database)
#CMD: python manage.py loaddata database_data.json
#
#What to edit what populates the tables when performing loaddata
#edit the fixtures file located at .\theTheatre\theTheatre\database\fixtures\database_test.json
#
#
#ask about this first before messing with:
#migrations are used to switch between different setups for the tables
#this includes things like renaming, adding, removing rows and changing the conditions for data, etc
#
#how to make a new migration (each migration is listed by a number 'xxxx')
#migations are useful for editing the model
#
#CMD: python manage.py makemigration <appname>
#	python manage.py makemigrations database
#
#how to migrate to a migration('xxxx' is the migration number)
#
#CMD: python manage.py sqlmigrate <appname> xxxx
#	python manage.py sqlmigrate database 0002
#
#CMD: python manage.py migrate