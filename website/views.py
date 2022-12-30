from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from website.models import contact
from website.forms import NameForm,contactform,NewsLetterForm
from django.http import HttpResponseRedirect
from django.contrib import messages


def index_views(requests):
    return render(requests,'website/index.html')

def about_views(request):
    return render(request,'website/about.html')

def contact_views(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your ticket sumbited successfully')
        else :
            messages.add_message(request,messages.ERROR,'Your ticket did not submite')
    form = contactform()
    return render(request,'website/contact.html',{'form':form})

def newsletter_views(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
        return  HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
            
        

def test_views(request):
    if request.method == 'POST':
        form = contactform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('success')
        else:
            return HttpResponse('error')
       
    form = contactform()
    return render(request,'test.html',{'form':form})
    