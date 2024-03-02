from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import*
from .forms import CategoryForm
from django.contrib import messages # yo chai messages ko laagi predefined huncha

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

# to show category form and post category
def addCategory(request):
     # data processing
     if request.method == 'POST':
          form = CategoryForm(request.POST)
          if form.is_valid():
               form.save()
               messages.add_message(request, messages.SUCCESS,'Category added successfully')
               return redirect('/products/addcategory')
          else:
               messages.add_message(request,messages.ERROR,'Failed to add category')
               return render(request,'products/addcategory.html',{'forms':form}) 

     context={
          'forms':CategoryForm
     }

     #to load add category form
     return render(request,'products/addcategory.html',context)
