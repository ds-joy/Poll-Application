from django.shortcuts import render
from .models import Product

# Create your views here.
def product_detail_view(response, *args, **kwargs):

    obj = Product.objects.get(id=1)

    details = {
        "title" : obj.title,
        "price" : obj.price,
    }
    return render(response, "products/detail.html", details)
