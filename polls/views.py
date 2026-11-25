from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse #Imports Django’s HttpResponse, which lets you create a response to send to the browser.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")