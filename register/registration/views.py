from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.urls import reverse
from django.contrib import messages
# from django.contrib.auth.backends import ModelBackend
# Create your views here.

# here u can controll or change any thing
def login_page(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        username = User.objects.get(email=email.lower()).username
        user =auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect(reverse('welcome_page'))
        else:
            messages.info(request,'Invalid Email/Password!') 
            return redirect(reverse('login_page'))
    else:
       return render(request,'login.html')    

def registration(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2'] 

        if password1 != password2:
            messages.info(request, 'Password not matching') 
            return redirect(reverse('register_page'))       
        
        elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect(reverse('register_page'))

        elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect(reverse('register_page'))

        else:
            messages.info(request, 'User Created') 
            user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
            user.save();
            print("user created")
            return redirect(reverse('login_page'))
         
           
    else:    

        return render(request,'register.html')

# For view u nedd add new function
def home_view(request):
    return render(request,'home.html')
def welcome_page(request):
    messages.info(request,'You are logged in')
    return render(request,'welcome.html')
def logout(request):
    auth.logout(request)
    return redirect(reverse('home_page'))    

