from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import BlogModel

# Create your views here.
def index(request):
    return render(request,"hello/index.html")

def concept(request):
    return render(request,"hello/concept.html")

def location(request):
    return render(request,"hello/location.html")
