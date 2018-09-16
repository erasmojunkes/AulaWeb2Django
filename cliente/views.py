from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
import datetime

def home(request):
    return render(request, 'cliente.html')