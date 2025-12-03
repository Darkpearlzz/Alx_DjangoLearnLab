from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    posts = Post.objects.filter(is_published=True)
    return render(request, "blog/index.html", {"posts": posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, is_published=True)
    return render(request, "blog/post_detail.html", {"post": post})
