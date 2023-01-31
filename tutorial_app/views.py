from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import BlogModel
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,"hello/index.html")

def concept(request):
    return render(request,"hello/concept.html")

def login(request):
    return render(request, 'hello/login.html')

@login_required
def location(request):
    return render(request,"hello/location.html")

def blank(request):
    return render(request,"hello/blank.html") 

def pale(request):
    return render(request,"hello/pale.html")

class BlogList(ListView):
    template_name = "list.html"
    model = BlogModel
