from django import forms
from  website.models import contact,NewLetter
from captcha.fields import CaptchaField

class NameForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)


class CaptchaTestModelForm(forms.ModelForm):
    captcha = CaptchaField()


class contactform(forms.ModelForm):
    CaptchaField()
    class Meta:
        model = contact
        fields = '__all__'

class NewsLetterForm(forms.ModelForm):

    class Meta:
        model = NewLetter
        fields = '__all__'