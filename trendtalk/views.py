from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # Additional logic for handling likes, comments, etc.
    return render(request, 'post_detail.html', {'post': post})

 


@login_required
def profile(request):
    return render(request, 'profile.html')