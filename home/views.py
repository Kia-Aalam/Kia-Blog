from django.shortcuts import render, redirect
from .models import Post, Category, SocialMediaLink, Message, Like
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def home(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, 'index.html', context={'posts':posts, 'categories': categories})

def about(request):
    return render(request, 'about.html')

# ---
def blog(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    recent_posts = Post.objects.all().order_by('-date')[:5]
    # Search
    q = request.GET.get('q')
    if q :
        posts = Post.objects.filter(title__icontains=q)
    # Pagination
    page = request.GET.get('page')
    paginator = Paginator(posts, 2)
    page_paginator = paginator.get_page(page)
    
    return render(request, 'blog.html', context={'posts':page_paginator, 'categories': categories, 'recent_posts': recent_posts})

def category_recent(request, slug):
    recent_posts = Post.objects.all().order_by('-date')[:5]
    categories = Category.objects.all()
    
    category = get_object_or_404(Category, slug=slug)
    posts = category.post_set.all()

    return render(request, 'blog.html', context={'posts':posts, 'categories': categories, 'recent_posts': recent_posts})
# ---

def post_details(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.view += 1
    post.save()
    
    categories = Category.objects.all()
    recent_posts = Post.objects.exclude(id=post.id).order_by('-date')[:5]
    
    social_media_links = SocialMediaLink.objects.filter(post=post)

    # Like
    if request.user.is_authenticated:
        user_liked = Like.objects.filter(
            user=request.user,
            post=post
        ).exists()
    else:
        user_liked = False
    
    return render(request, 'post-details.html' , context={'post':post, 'categories': categories, 'recent_posts': recent_posts, 'social_media_links': social_media_links, 'user_liked':user_liked })

@login_required
def LikeView(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    like = Like.objects.filter(user=request.user, post=post)
    if like.exists():
        like.delete()
    else:
        Like.objects.create(user=request.user, post=post)
    
    return redirect('post-details', slug=post.slug)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        if name and email and subject and message:
            new_message = Message(name=name, email=email, subject=subject, message=message)
            new_message.save()
            
            messages.success(request, "Your message has been sent successfully!")
        else:
            messages.error(request, "Your message could not be sent! Please again send your message.")
        
    return render(request, 'contact.html')