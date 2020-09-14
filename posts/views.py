from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

# Create your views here.

class PostListView(ListView):
    context_object_name = 'all_posts'
    model = Post
    template_name = 'posts/index.html'
