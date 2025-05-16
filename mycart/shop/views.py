from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.

def index(request):
    products = Product.objects.all()
    print(products)
    n=len(products)
    num_slides = n//4 + ceil((n/4)-(n//4))
    dic = {'product':products,'num_slide':num_slides,'range':range(1,num_slides)}
    return render(request,'shop/index.html',dic)
def about(request):
    return render(request,'shop/about.html')
def contact(request):
    return HttpResponse("This is contact")
    #return render(request,'shop/contact.html')
def tracker(request):
    return HttpResponse("This is tracker")
    #return render(request,'shop/track.html')
def search(request):
    return HttpResponse("This is search")
    #return render(request,'shop/search.html')
def productview(request):
    return HttpResponse("This is productview")
    #return render(request,'shop/productview.html')
def checkout(request):
    return HttpResponse("This is checkout")
    #return render(request,'shop/checkout.html')
