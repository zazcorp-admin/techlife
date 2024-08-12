from django.shortcuts import render
from pyexpat.errors import messages

from .forms import BlogPostForm
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


def add_blog(request):
    form = BlogPostForm()
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            fm = form.save(commit=False)
            fm.save()
            fm.save_m2m()
            messages.success(request, 'Your post has been added.')
        else:
            messages.warning(request, 'Something went wrong. Please try again.')

    context = {
        'form': form,
    }
    return render(request, 'core/add_blog.html', context)
