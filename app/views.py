from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from .models import *


def ProfileView(request):
    profile = Profile.objects.get(id=request.user.id)
    # blog = Post.objects.select_related('user', 'category').prefetch_related('tags')
    blog = Post.objects.filter(user = request.user)
    
    return render(request, 'blog/profile.html', {'profile': profile})


def BlogView(request):
    blog = Post.objects.all().select_related('user', 'category').prefetch_related('tags')
    return render(request, 'blog/blog.html', {'blog': blog})


def DetailBlogView(request, pk):
    blog = Post.objects.select_related('user', 'category').prefetch_related('tags').get(id=pk)
    return render(request, 'blog/detail_blog.html', {'b': blog})