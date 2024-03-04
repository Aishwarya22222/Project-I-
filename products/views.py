from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
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

# adding product
def postProduct(request): 
     if request.method == 'POST':
          form = ProductForm(request.POST, request.FILES)
          if form.is_valid():
               form.save()
               messages.add_message(request, messages.SUCCESS, 'Product added successfully')
               return redirect('/products/show')
          else:
               messages.add_message(request,messages.ERROR,'Failed to add product')
               return render(request,'products/addproduct.html',{'forms':form}) 

     context={
          'forms':ProductForm
     }

     #to load add category form
     return render(request,'products/addproduct.html',context)


# allcategory dekhaune function
def showcategory(request):
     category = Category.objects.all()
     context = {
          'categories':category
     }
     return render(request,'products/allcategory.html',context)

# delete category
def deletecategory(request,category_id):
     category=Category.objects.get(id=category_id)
     category.delete()
     messages.add_message(request,messages.SUCCESS,'Category successfully deleted')
     return redirect('/products/allcategory')

# update category ko form dekhaune and update
def updatecategory(request,category_id):
     instance = Category.objects.get(id=category_id)

     if request.method == 'POST':
          form = CategoryForm(request.POST,instance=instance)
          if form.is_valid():
              form.save()
              messages.add_message(request, messages.SUCCESS, 'Category Update')
              return redirect('/products/allcategory')
          else:
               messages.add_message(request,messages.ERROR,'Failed to update category')
               return render(request,'products/updatecategory.html',{'forms':form}) 

     context ={
          'forms':CategoryForm(instance = instance)
     }
     return render(request,'products/updatecategory.html',context)

# delete product
def deletecategory(request,product_id):
     product=Product.objects.get(id=product_id)
     product.delete()
     messages.add_message(request,messages.SUCCESS,'Product successfully deleted')
     return redirect('/products/show')

# update product
def updateproduct(request, product_id):
     instance = Product.objects.get(id=product_id)

     if request.method == 'POST':
          form = ProductForm(request.POST,instance=instance)
          if form.is_valid():
              form.save()
              messages.add_message(request, messages.SUCCESS, 'Product Update')
              return redirect('/products/show')
          else:
               messages.add_message(request,messages.ERROR,'Failed to update product')
               return render(request,'products/updateproduct.html',{'forms':form}) 

     context ={
          'forms':ProductForm(instance = instance)
     }
     return render(request,'products/updateproduct.html',context)







