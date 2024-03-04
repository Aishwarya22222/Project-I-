from django.shortcuts import render
from products.models import Product

# Create your views here.
def homepage(request):
    products = Product.objects.all() #database bata data fetch gareko
    context={
        'products':products
    }
    return render(request,'userpage/home.html',context)

