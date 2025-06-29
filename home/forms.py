from django import forms
from django.forms import ModelForm
from .models import News, NewsImage

class NewsForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"News title"}))
    text = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "placeholder":"News description"}))
    image = forms.ImageField(widget=forms.FileInput(attrs={"class":"form-control"}))
    social_website = forms.URLField(widget=forms.URLInput(attrs={"class":"form-control", "placeholder":"News title"}))

    class Meta:
        model = News
        exclude = ['news_view']
    
  


class ImageForm(ModelForm):
    images = forms.ImageField(widget=forms.FileInput(attrs={"class":"form-control", "multiple": True}))
    class Meta:
        model = NewsImage
        fields = ['images']
