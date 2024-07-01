from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from . models import customer
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
def sing_out(request):
    logout(request)
    return redirect('home')
# Create your views here.
def show_account(request):
    context={}
    if request.POST and 'register' in request.POST:
        context['register']=False
        try:
            
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            address=request.POST.get('address')
            phone=request.POST.get('phone')
            #create user accounts
            user=user.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            #create customer account
            customer=customer.objects.create(
                name=username,
                user=user,
                phone=phone,
                address=address
            )
            success_messages="User Registered Successfully"
            messages.success(request,"success_message")
        except Exception as e:
            error_message="Duplicate username or invalid inputs"
            messages.error(request,error_message)
    if request.POST and 'login' in request.POST:
        context['register']=False
        print(request.POST)
        username=request.POST.get['username']
        password=request.POST.get['password']
        print(username,password)
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            redirect('home')
        else:
            messages.error(request,'invalid user credentials')    
    return render(request,'account.html',context)