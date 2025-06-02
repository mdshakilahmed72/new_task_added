from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Home(request):
    return HttpResponse("Hello this is a My Name is  Shakil")

def Contact(request):
    return HttpResponse("Hello Bangladesh is Really FLood Coutry")