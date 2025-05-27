from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
def home(request):
 return render(request, 'home.html')

def abaout(request):
 return render(request, 'abaout.html' )