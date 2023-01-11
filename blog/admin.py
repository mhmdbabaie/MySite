from django.contrib import admin
from blog.models import Post,Category,Comments
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = 'empty'
    list_display = ('title','author','counted_views','status','published_date')
    list_filter = ('status','author')
    summernote_fields = ('content')
    search_fields = ['title','content']

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name','post','approach','created_date')
    list_filter = ('post','approach')
    search_fields = ['name','post']

admin.site.register(Comments,CommentAdmin)
admin.site.register(Category)
admin.site.register(Post,PostAdmin)        