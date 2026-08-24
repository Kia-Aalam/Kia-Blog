from django.db import models
from datetime import date
from django.conf import settings # User
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Category name")
    slug = models.SlugField(unique=True, blank=True, null=True)  
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
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
    category = models.ManyToManyField(Category, blank=True)
    writer = models.CharField(max_length=100)
    date = models.DateField(default=date.today)
    view = models.IntegerField(default=0)
    
    slug = models.SlugField(default="", null=False, unique=True)
    def save(self, *args, **kwargs):
        if not self.slug: 
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ('-id',)

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
    
class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="Likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="Likes")
    
    #created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "post"],
                name="unique_user_post_like"
            )
        ]