from django.shortcuts import render , get_object_or_404, redirect
from blog.models import Post,Comments 
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from blog.forms import commentsform
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect



def blog_view(requests,cat_name=None,author_username = None,**kwargs):
    posts = Post.objects.filter(status=1)
    if  cat_name:
        posts = Post.objects.filter(category_name=cat_name)
    if author_username:
        posts = Post.objects.filter(author__username=author_username)
    if kwargs.get('tag_name')!=None:
        pass
       # posts = Post.filter(author_username= kwargs['author_username'])
    posts = Paginator(posts,3)
    try:
        page_number =requests.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts': posts}
    return render(requests,'blog/blog-home.html',context)


def blog_single(request,pid):
    if request.method == 'POST':
        form = commentsform(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'your Comment sumbited successfully')
        else:
            messages.add_message(request,messages.ERROR,'your Comment didnt submited')
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts,pk=pid)
    if not post.login_required:
        comments = Comments.objects.filter(post=post.id,approved= True)
        form = commentsform()
        context = {'post': post , 'comments': comments, 'form': form}
        return render(request,'blog/blog-single.html',context)
    else:
        return HttpResponseRedirect(reverse('accounts:login'))

 
def test(requests,pid):
    #post = Post.objects.get(id=pid)
    post = get_object_or_404(Post, pk=pid)
    context = {'post': post} 
    return render(requests,'test.html',context) 

def blog_category(requests,cat_name):
    posts =Post.objects.filter(status=1)
    posts = Post.filter(category_name=cat_name)
    context = {'posts': posts}
    return render(requests,'blog/blog_home.html',context)

def blog_search(requests):
    posts = Post.objects.filter(status=1)
    if requests.method == 'GET':
        #print('request get')
        posts = posts.filter(content__contains=requests.GET.get('s'))
    context = {'posts': posts}
    return render(requests,'blog/blog-home.html',context)
    

