from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(req):
    return HttpResponse('Hello, World!')
  
def about(req):
    return render(req, 'about.html')