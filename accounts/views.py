from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from . forms import LoginForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def register_user(request):
    if(request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'New account created')
            return redirect('/register')
        else:
            messages.add_message(request,messages.ERROR,'Failed to create an account')
            return render(request,'accounts/register.html',{'forms':form})

    context={
        'forms': UserCreationForm  # inbuilt django forms ho, ani page dekhauna ko laagi haamile context define garnu parxa

    }
    return render(request,'accounts/register.html',context)

# Login-Form created
def post_login(request):
    if(request.method == 'POST'):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data # valid data maatra aaos vaneera cleaned data use gareko
            user = authenticate(request,username =data['username'],password =data['password'])

            if user is not None: # khaali chhaina vane
                login(request,user)
                if user.is_staff:
                    return redirect('/admins/dashboard')
                else:
                    return redirect('/') 
                
            else:

                messages.add_message(request,messages.ERROR,'Username or Password does not match')
                return render(request,'accounts/login.html',{'forms':form})
    context={
        'forms':LoginForm
    }

    return render(request,'accounts/login.html',context)

def logout_user(request):
    logout(request)
    return redirect('/login')
