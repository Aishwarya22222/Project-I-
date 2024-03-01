from django.shortcuts import render
from django.http import HttpResponse
from .models import*
from .forms import CategoryForm

# Create your views here.
def index(request):
     return HttpResponse('This is from the product app')

# to fetch all data from the database
def showproduct(request):
     products = Product.objects.all()
     context = {
          'products':products
     }
     return render(request,'products/product.html',context)

# to sow category form and post category
def addCategory(request):

     context={
          'forms':CategoryForm
     }
     return render(request,'products/addcategory.html',context)
