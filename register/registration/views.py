from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.urls import reverse
from django.contrib import messages
# Create your views here.

# here u can controll or change any thing
def registration(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2'] 

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect(reverse('register_page'))

            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect(reverse('register_page'))

            else:
                user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                user.save();
                print("user created")
                return redirect(reverse('home_page'))
        else: 
            messages.info(request, 'Password not matching') 
            return redirect(reverse('register_page'))       
    else:    

        return render(request,'register.html')

# For view u nedd add new function
def home_view(request):
    return render(request,'home.html')