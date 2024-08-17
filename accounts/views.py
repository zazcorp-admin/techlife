from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from core.models import Category, BlogPost, Tag


# Create your views here.
def signup_page(request):
    if request.method == 'POST':
        full_name = request.POST.get('fullName')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        # Check if a user with this email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'User with this email already exists')
            return HttpResponseRedirect(request.path_info)

        if pass1 != pass2:
            messages.error(request, 'Passwords do not match')
            return HttpResponseRedirect(request.path_info)

        # Split full name into first and last name
        name_parts = full_name.split()
        first_name = name_parts[0]
        last_name = ' '.join(name_parts[1:]) if len(name_parts) > 1 else ''

        # Create new user
        user = User.objects.create_user(username=email, email=email, password=pass1,
                                        first_name=first_name, last_name=last_name)
        messages.success(request, 'Account created successfully')  # Assuming you have a login page

    return render(request, 'accounts/signup.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        if not User.objects.filter(username=username).exists():
            messages.error(request, 'User with this username does not exist')

        user_obj = authenticate(request, username=username, password=password)
        if user_obj:
            login(request, user_obj)
            return redirect('/')
        else:
            messages.warning(request, 'invalid credentials')
            return HttpResponseRedirect(request.path_info)


    return render(request, 'accounts/login.html')

def logout_page(request):
    logout(request)
    return redirect('/')


def dashboard(request):
    categories = Category.objects.all().order_by('-created_at')
    blogs_posts = BlogPost.objects.all().order_by('-created_at')
    tags = Tag.objects.all().order_by('-created_at')

    if request.method == 'POST':
        tag_name = request.POST.get('tag_name')

        if len(tag_name) > 0:
            tag = Tag.objects.create(tag_name=tag_name)
            tag.save()
            return HttpResponseRedirect(request.path_info)
        else:
            print("Something went wrong")


    context = {
        'categories': categories,
        'blogs_posts': blogs_posts,
        'tags': tags
    }

    return render(request, 'accounts/dashboard.html', context)




def custom_404_view(request, exception):
    return render(request, 'base/new_404.html', status=404)




