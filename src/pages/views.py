from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(response, *args, **kwargs):
    return HttpResponse("<h1>Home page<h1>")

def about_view(response, *args, **kwargs):
    return HttpResponse("<h1>About Page<h1>")

def contacts_view(response, *args, **kwargs):
    return HttpResponse("<h1>Contact Page<h1>")
