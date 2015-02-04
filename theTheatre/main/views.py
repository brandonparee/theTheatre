from django.shortcuts import render
from django.http import HttpResponse

from database.models import Performance, Merchandise, TicketSale

def home(request):
	return render(request, 'main/index.html', {})

def about(request):
	return render(request, 'main/about.html', {})

def performances(request):
	return render(request, 'main/performances.html', {})

def merch(request):
	return render(request, 'main/merch.html', {})

def sales(request):
	return render(request, 'main/sales.html', {})