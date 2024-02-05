from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(request):
     return HttpResponse('This is from the product app')

def showproduct(request):
     products = Product.objects.all()
     context = {
          'products':products
     }
