from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return render(request, 'blog/main.html')

def products(request):
	return render(request, 'blog/login.html')

def customer(request):
	return render(request, 'blog/offerings.html')
