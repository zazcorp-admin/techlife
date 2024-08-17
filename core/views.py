from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages

from .forms import BlogPostForm, CategoryForm
from .models import BlogPost, Category, Tag
from django.db.models import Q


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
    categories = Category.objects.all()
    context = {
        'blog': blog,
        'categories': categories,
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


def add_category(request):

    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            fm = form.save(commit=False)
            fm.save()
            messages.success(request, 'Your category has been added.')
            return redirect('dashboard')
        else:
            print(form.errors)
            messages.warning(request, 'Something went wrong. Please try again.')

    else:
        form = CategoryForm()
    context = {
        'form':form
    }
    return render(request, 'core/add_category.html', context)



def delete_category(request, slug):
    category = Category.objects.get(slug=slug)
    category.delete()
    return redirect('dashboard')

def edit_category(request, slug):
    category = Category.objects.get(slug=slug)
    form = CategoryForm(instance=category)
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            print(form.errors)
            return HttpResponseRedirect(request.path_info)
    else:
        form = CategoryForm(instance=category)

    context ={
        'form':form
    }
    return render(request, 'core/add_category.html', context)


def edit_blog(request, slug):
    blog = BlogPost.objects.get(slug=slug)
    form = BlogPostForm(instance=blog)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            print(form.errors)
            return HttpResponseRedirect(request.path_info)
    else:
        form = BlogPostForm(instance=blog)

    context = {
        'form': form,
    }
    return render(request, 'core/add_blog.html', context)

def delete_blog(request, slug):
    blog = BlogPost.objects.get(slug=slug)
    blog.delete()
    return redirect('dashboard')


def delete_tag(request, slug):
    tag = Tag.objects.get(slug=slug)
    tag.delete()
    return redirect('dashboard')


def search_results(request):
    query = request.GET.get('q')
    results = None
    if query:
        results = BlogPost.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    context = {
        'query': query,
        'results': results
    }
    return render(request, 'core/search.html', context)

