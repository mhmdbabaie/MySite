from django.shortcuts import render , get_object_or_404
from blog.models import Post 




def blog_view(requests):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(requests,'blog/blog-home.html',context)


def blog_single(requests,pid):
    post = get_object_or_404(Post, pk=pid,status=1)
    context = {'post': post}
    return render(requests,'blog/blog-single.html',context)
 
def test(requests,pid):
    #post = Post.objects.get(id=pid)
    post = get_object_or_404(Post, pk=pid)
    context = {'post': post} 
    return render(requests,'test.html',context) 
