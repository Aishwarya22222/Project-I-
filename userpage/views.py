from django.shortcuts import render,redirect
from products.models import Product
from django.contrib.auth.decorators import login_required
from .models import Cart
from django.contrib import messages
from .forms import*


# Create your views here.
def homepage(request):
    products = Product.objects.all().order_by('-id')[:8] #database bata data fetch gareko, order by id in descendinbg order,
    context={
        'products':products
    }
    return render(request,'userpage/home.html',context)


# product details
def productdetails(request,product_id):
    product=Product.objects.get(id=product_id)
    context={
        'product':product
    }
    return render(request,'userpage/productdetails.html',context)

# sabai product show garna ko laagi
def show_products(request):
    products=Product.objects.all()
    context={
        'products':products
    }
    return render(request,'userpage/products.html',context)

# login nagari access garna namilne function create
@login_required
def add_to_cart(request,product_id):
    user=request.user
    product=Product.objects.get(id=product_id)
    check_items_present=Cart.objects.filter(user=user,product=product)
    if check_items_present:
        messages.add_message(request,messages.ERROR,'Product already in the cart')
        return redirect('/cart')
    else:
        cart=Cart.objects.create(product=product,user=user)
        if cart:
            messages.add_message(request,messages.SUCCESS,'product added to cart')
            return redirect('/cart')
        else:
            messages.add_message(request,messages.ERROR,'Something went wrong')
            return redirect('/product')
        

# jasle login gareko cha tei user dekhina ko laagi banaako function
@login_required
def show_cart_items(request):
    user=request.user
    cart=Cart.objects.filter(user=user)
    context={
        'cart':cart
    } 
    return render(request,'userpage/cart.html',context)


# items in cart deleting function
@login_required
def delete_cart_item(request, cart_id):
    cart=Cart.objects.get(id= cart_id)
    cart.delete()
    messages.add_message(request,messages.SUCCESS,'Cart-item is deleted')
    return redirect('/cart')

#creating function for orderform 
@login_required
def order_item(request,product_id,cart_id):
    user=request.user
    product=Product.objects.get(id=product_id)
    cart_item=Cart.objects.get(id=cart_id)

    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            quantity=request.POST.get('quantity')
            price=product.product_price
            total_price=int(quantity)*int(price)
            phone_no=request.POST.get('phone_no')
            address=request.POST.get('address')
            payment_method=request.POST.get('payment_method')
            payment_status=request.POST.get('payment_status')

            #order create gareko(left sideko chai model ko attribute ko name ho ani right side ko chai variable ho)
            order=Order.objects.create(
                product=product,
                user=user,
                quantity=quantity,
                total_price=total_price,
                phone_no=phone_no,
                address =address,
                payment_method=payment_method,
                payment_status=payment_status
            )
            if order.payment_method=='Cash On Delivery':
                cart=Cart.objects.get(id=cart_id)
                cart.delete()
                messages.add_message(request,messages.SUCCESS,'Order Success')
                return redirect('/myorder')
            elif order.payment_method=='Esewa':
                context={
                    'order':order,
                    'cart':cart_item
                }
                return render(request,'userpage/esewa_payment.html',context)
            else:
                messages.add_message(request,messages.ERROR,'Something went wrong')
                return render(request,'userpage/orderform.html',{'forms':order})

    context={
        'forms':OrderForm
    }
    return render(request,'userpage/orderform.html',context)

#creating function for my order
@login_required
def my_order(request):
    user=request.user
    order=Order.objects.filter(user=user)

    context={
        'items':order
    }

    return render(request,'userpage/myorder.html',context)

    



        





