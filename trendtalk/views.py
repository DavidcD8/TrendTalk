from .forms import ProfilePhotoForm  # Import your ProfilePhotoForm
from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .models import Post, Comment
from .forms import CommentForm, ProfilePhotoForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import ProfilePhotoForm
from .models import Profile


class PostListView(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "post_list.html"
    context_object_name = "posts"
    paginate_by = 10


class PostDetailView(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLikeView(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def profile(request):
    user_comments = Comment.objects.filter(email=request.user.email)
    return render(request, 'profile.html', {'user_comments': user_comments})


@login_required
def edit_profile(request):
    current_user = request.user

    try:
        profile = Profile.objects.get(user=current_user)
    except Profile.DoesNotExist:
        # If the profile doesn't exist, create one
        profile = Profile.objects.create(user=current_user)

    if request.method == 'POST':
        user_form = UserChangeForm(request.POST, instance=current_user)
        profile_form = ProfilePhotoForm(
            request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your Profile has been updated!")
            return redirect("edit_profile")
    else:
        user_form = UserChangeForm(instance=current_user)
        profile_form = ProfilePhotoForm(instance=profile)

    return render(
        request,
        "edit_profile.html",
        {"user_form": user_form, "profile_form": profile_form},
    )


@login_required
def settings(request):
    # Your view logic here
    return render(request, 'settings.html')  # Replace with the actual template name