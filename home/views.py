from django.shortcuts import render
from .models import Post, Category

def home(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, 'index.html', context={'posts':posts, 'categories': categories})

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def post_details(request):
    # views
    return render(request, 'post-details.html')

def contact(request):
    return render(request, 'contact.html')