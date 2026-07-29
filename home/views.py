from django.shortcuts import render
from .models import Post, Category, SocialMediaLink, Message
from django.shortcuts import get_object_or_404
from django.contrib import messages

def home(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, 'index.html', context={'posts':posts, 'categories': categories})

def about(request):
    return render(request, 'about.html')

#
def blog(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    recent_posts = Post.objects.all().order_by('-date')[:5]
    
    return render(request, 'blog.html', context={'posts':posts, 'categories': categories, 'recent_posts': recent_posts})

def category_recent(request, id):
    recent_posts = Post.objects.all().order_by('-date')[:5]
    categories = Category.objects.all()
    
    category = get_object_or_404(Category, id=id)
    posts = category.post_set.all()

    return render(request, 'blog.html', context={'posts':posts, 'categories': categories, 'recent_posts': recent_posts})
#

def post_details(request, id):
    post = get_object_or_404(Post, id=id)
    post.view += 1
    post.save()
    
    categories = Category.objects.all()
    recent_posts = Post.objects.exclude(id=id).order_by('-date')[:5]
    
    social_media_links = SocialMediaLink.objects.filter(post=post)
    
    return render(request, 'post-details.html', context={'post':post, 'categories': categories, 'recent_posts': recent_posts, 'social_media_links': social_media_links })

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