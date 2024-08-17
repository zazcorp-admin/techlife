from django import forms
from .models import BlogPost, Category
from django.contrib.auth.models import User
from django_summernote.widgets import SummernoteWidget
from django_summernote.fields import SummernoteTextField

class BlogPostForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title', 'id': 'postTitle'})
    )
    content = SummernoteTextField()
    author = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    category = forms.ModelChoiceField(
        queryset= Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-label', 'for': 'postCategory', 'placeholder':'Select a category'})
    )
    cover_pic = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control', 'type':'file', 'id':'postImage', 'accept': "image/*"})
    )

    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'author', 'tags', 'cover_pic', 'category']
        widgets = {
            'content': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(BlogPostForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field != 'content' and field != 'cover_pic':
                self.fields[field].widget.attrs.update({'class': 'form-control'})

class CategoryForm(forms.ModelForm):
    category_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter category', 'id': 'categoryName'})
    )
    category_pic = forms.ImageField(
        required=True,
        widget=forms.FileInput(attrs={'class': 'form-control', 'type': 'file', 'accept': "image/*"})
    )
    class Meta:
        model = Category
        fields = ['category_name', 'category_pic']