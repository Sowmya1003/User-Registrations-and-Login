from django.shortcuts import render,redirect
from .models import Person_data
# Create your views here.
def registration(request):
    person1 = Person_data()
    return render(request, 'home.html')