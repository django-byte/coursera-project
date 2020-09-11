from django.shortcuts import render, get_object_or_404
from .models import Post


def home(request):
    posts = Post.objects.all()

    return render(request, 'home.html', {'section': 'home', 'posts': posts})


def detail(request, slug=None):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'detail.html', {'section': 'blog_detail', 'post': post, })
