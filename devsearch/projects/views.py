from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def projects(request):
    return HttpResponse("This is Projects Section...")