from django.shortcuts import render
from django.http import HttpResponse

def index_views(requests):
    return render(requests,'website/index.html')

def about_views(request):
    return render(request,'website/about.html')

def contact_views(request):
    return render(request,'website/contact.html')

def test_views(requests):
    contex = {'title': 'my name is mhmd babaie and im working in izbank', 'edu':'my education is software engineering'}
    return render(requests,'website/test.html',contex)

