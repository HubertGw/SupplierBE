from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home_widok(*args, **kwargs):
    return HttpResponse("<h1>Hello world!</h1>")
