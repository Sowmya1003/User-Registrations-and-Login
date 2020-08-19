from django.shortcuts import render,redirect

# Create your views here.
def registration(request):
    return render(request, 'register.html')