from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "home/index.html")

def birth(request):
    return render(request, "home/birth.html")

def livesin(request):
    return render(request, "home/livesin.html")

def plots(request):
    return render(request, "home/plots.html")
# Create your views here.
