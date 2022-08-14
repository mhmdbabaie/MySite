from django.shortcuts import render
from django.http import HttpResponse

def index_views(requests):
    return render(requests,'index.html')

def about_views(request):
    return render(request,'about.html')

def contact_views(request):
    return render(request,'contact.html')


