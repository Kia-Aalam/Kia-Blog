from django.contrib import admin
from .models import Post, Category, SocialMediaLink, Message, Like

class SocialMediaLinkInline(admin.TabularInline):
    model = SocialMediaLink
    extra = 1 

class PostAdmin(admin.ModelAdmin):
    inlines = [SocialMediaLinkInline]
    list_display = ("title",)
    prepopulated_fields = {"slug": ("title",)}
    
class CategoryAdmin(admin.ModelAdmin):  
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SocialMediaLink)
admin.site.register(Message)
admin.site.register(Like)