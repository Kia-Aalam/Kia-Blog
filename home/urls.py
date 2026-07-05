from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('post_details/', views.post_details, name='post-details'),
    path('contact/', views.contact, name='contact'),
]