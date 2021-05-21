from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(response, *args, **kwargs):
    # return HttpResponse("<h1>Home page<h1>")
    #using django template
    return render(response, "home.html", {}) 

def about_view(response, *args, **kwargs):

    about_me = {
        "name" : "Debasish Sarker",
        "age" : 23,
        "my_list" : ["apple", "orange", "banana"],
    }
   
    return render(response, "about.html", about_me)




def contacts_view(response, *args, **kwargs):
    return render(response, "contacts.html", {})

def features_view(response, *args, **kwargs):
    return render(response, "features.html", {})
