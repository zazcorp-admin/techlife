from django.shortcuts import render, redirect
from django.contrib import messages

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
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            fm = form.save(commit=False)
            fm.author = request.user
            fm.save()
            messages.success(request, 'Your post has been added.')
            return redirect('dashboard')  # Replace with your actual URL name
        else:
            print(form.errors)
            messages.warning(request, 'Something went wrong. Please try again.')
    else:
        form = BlogPostForm()

    context = {
        'form': form,
    }
    return render(request, 'core/add_blog.html', context)
