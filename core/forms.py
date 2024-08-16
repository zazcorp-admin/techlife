from django import forms
from .models import BlogPost, Category
from django.contrib.auth.models import User
from taggit.forms import TagField
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
    tags = TagField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter tags separated by commas',
            'id':  'postTags'
        })
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

    # def clean_tags(self):
    #     tags = self.cleaned_data.get('tags')
    #     if tags:
    #         tags = [tag.strip().lower() for tag in tags.split(',') if tag.strip()]
    #     return tags