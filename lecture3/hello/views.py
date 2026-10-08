from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, World")

def brian(request):
    return HttpResponse("hello, Brian!")

def ayman(request):
    return HttpResponse("hello, Ayman!")

def greet(request, name):
    return HttpResponse(f"hello, {name}!")
