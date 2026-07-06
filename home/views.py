from django.shortcuts import render
from .models import Post, Category, Message
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
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        if name and email and subject and message:
            new_message = Message(name=name, email=email, subject=subject, message=message)
            new_message.save()
            
    return render(request, 'contact.html')