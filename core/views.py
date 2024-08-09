from django.shortcuts import render
from .models import BlogPost, Category


def index(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'core/index.html', context)


def post_list(request):
    blogs = BlogPost.objects.all()
    categories = Category.objects.all()
    context = {
        'blogs': blogs,
        'categories': categories
    }
    return render(request, 'core/post_list.html', context)


def post_details(request, slug):
    blog = BlogPost.objects.get(slug=slug)
    context = {
        'blog': blog,
    }
    return render(request, 'core/post_details.html', context)
