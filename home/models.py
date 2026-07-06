from django.db import models
from datetime import date

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Category name")
    slug = models.SlugField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='img',
        null=True,
        blank=True
    )
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    writer = models.CharField(max_length=100)
    date = models.DateField(default=date.today)
    view = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
class SocialMediaLink(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='social_media_links')
    name = models.CharField(max_length=50) 
    url = models.URLField()

    def __str__(self):
        return f"{self.name} - {self.post.title}"
    
class Message(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    
    def __str__(self):
        return f"{self.name}/{self.subject[:10]}"