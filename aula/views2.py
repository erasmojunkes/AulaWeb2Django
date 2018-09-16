from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

def teste0 (request):
    x = "testando 0"
    return HttpResponse(x)

def teste1 (request):
    y = "testando 1"
    return HttpResponse(y)

def teste2 (request):
    z = "testando 2"
    return HttpResponse(z)

