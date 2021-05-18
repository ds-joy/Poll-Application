from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(response, *args, **kwargs):
    return HttpResponse("<h1>Home page<h1>")
