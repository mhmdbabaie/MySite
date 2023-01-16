from django import forms
from  blog.models import Comments



class commentsform(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['post','name','email','subject','meesage']