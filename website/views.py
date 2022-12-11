from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from website.models import contact

def index_views(requests):
    return render(requests,'website/index.html')

def about_views(request):
    return render(request,'website/about.html')

def contact_views(request):
    return render(request,'website/contact.html')

def test_views(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        c = contact()
        c.name = name
        c.email = email
        c.subject = subject
        c.message = message
        c.save()
        print (name, email, subject, message)
    return render(request,'test.html',{})

