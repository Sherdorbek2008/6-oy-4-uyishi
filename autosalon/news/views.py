from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from .models import Brand,Cars
# Create your views here.

def index(request:WSGIRequest):
    posts=Cars.objects.all()
    context={
        'posts':posts
    }

    return render(request,'index.html',context)