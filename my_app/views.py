from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore

# Create your views here.
def home(req):
    return HttpResponse('Hello, World!')
  
def about(req):
    return render(req, 'about.html')