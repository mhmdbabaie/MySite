from django import template
from blog.models import Post 
from blog.models import Category

register = template.Library()

@register.simple_tag(name='totalposts')
def function():
    posts = Post.objects.filter(status=1).count()
    return posts

@register.simple_tag(name='posts')
def function():
    posts = Post.objects.filter(status=1)
    return posts

@register.filter 
def snippet(value,args=100):
    return value[:args] + "..."

@register.inclusion_tag('blog/blog-popular-posts.html') 
def latestposts():
    posts = Post.objects.filter(status=1).order_by("published_date")
    return {'posts': posts}  

@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict ={}
    for name in categories:
        cat_dict[name] =posts.filter(Category=name).count()
    return {'categories': cat_dict}













    
# اینجا واسه قسمت سیمپل تگ میباشد که از طرق پیج تست کوِری میزنیم