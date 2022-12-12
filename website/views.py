from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from website.models import contact
from website.forms import NameForm

def index_views(requests):
    return render(requests,'website/index.html')

def about_views(request):
    return render(request,'website/about.html')

def contact_views(request):
    return render(request,'website/contact.html')

def test_views(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponse('success')
        else:
            return HttpResponse('error')
       
    form = NameForm()
    return render(request,'test.html',{'form':form})
    