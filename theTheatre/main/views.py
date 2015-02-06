from django.shortcuts import render
from django.http import HttpResponse

from database.models import Performance, Merchandise, TicketSale

def home(request):
	return render(request, 'main/index.html', {})

def about(request):
	return render(request, 'main/about.html', {})

def performances(request):
	performances = Performance.objects.all()
	
	test = {'Performance': performances}
	
	return render(request, 'main/performances.html', test)

def merch(request):
	return render(request, 'main/merch.html', {})

def sales(request):
	return render(request, 'main/sales.html', {})

#how to add entry to database:
    #1. from CMD "python manage.py shell"
    #2. from polls.models import Performance, Movie (or whatever table you want to work on)
    #3. new_addition = Performance(name="balh", date="12/12/1212", etc for all the fields)
    #4. new_addition.save() grats you added an entry to the database

#how to remove entry from the database:
    #1. from CMD "python manage.py shell"
    #2. from polls.models import Performance, Movie (or whatever table you want to work on)
    #3. new_array = Performance.objects.all()
    #4. new_array (this will list out all the elements in the array, find the one you want to delete)
    #5. new_array[3].delete() (this assumes you want to delete the fourth entry in the Performance)

#how to add table to the database:
    #1. Open polls\models.py
    #2. Create a new model (each model acts as a table)
    #3. from CMD "python manage.py check"
    #4. STOP if you have any errrors
    #5. "python manage.py migrate"