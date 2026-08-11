from django.contrib import admin
from .models import Post, Category, SocialMediaLink, Message, Like

class SocialMediaLinkInline(admin.TabularInline):
    model = SocialMediaLink
    extra = 1 

class PostAdmin(admin.ModelAdmin):
    inlines = [SocialMediaLinkInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(SocialMediaLink)
admin.site.register(Message)
admin.site.register(Like)