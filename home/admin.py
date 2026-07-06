from django.contrib import admin
from .models import Post, Category, Message

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Message)