from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Management resources")

def host_upload(request):
    return HttpResponse("Hello, world. Here you can update your data.")