from django.shortcuts import render
from .models import Post, Category
from django.shortcuts import get_object_or_404

def home(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, 'index.html', context={'posts':posts, 'categories': categories})

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def post_details(request, id):
    post = get_object_or_404(Post, id=id)
    post.view += 1
    post.save()
    
    categories = Category.objects.all()
    recent_posts = Post.objects.exclude(id=id).order_by('-date')[:5]
    
    return render(request, 'post-details.html', context={'post':post, 'categories': categories, 'recent_posts': recent_posts})

def contact(request):
    return render(request, 'contact.html')