from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Welcome to blogs-home</h1>')

def about(request):
    return HttpResponse('<h1>Welcome to blogs-about</h1>')
