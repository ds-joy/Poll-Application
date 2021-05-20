from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(response, *args, **kwargs):
    # return HttpResponse("<h1>Home page<h1>")
    #using django template
    return render(response, "home.html", {}) 

def about_view(response, *args, **kwargs):
    # return HttpResponse("<h1>About Page<h1>")
    return render(response, "about.html", {})
def contacts_view(response, *args, **kwargs):
    return render(response, "contacts.html", {})

def features_view(response, *args, **kwargs):
    return render(response, "features.html", {})
