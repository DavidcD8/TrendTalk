from django.http import Http404
from django.shortcuts import render
from .forms import ProfileEditForm
from .models import Post
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404
from .forms import CommentForm
from django.contrib.auth.forms import UserChangeForm
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .models import Comment
from django.contrib.auth.models import User
from .models import Profile


class WelcomeView(generic.TemplateView):  # Welcome Page view

    template_name = 'welcome.html'


class PostListView(generic.ListView):  # View for all Posts

    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "post_list.html"
    context_object_name = "posts"
    paginate_by = 10


class PostDetailView(View):  # View for the post details
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        # Get the latest 10 posts for the sidebar
        latest_posts = Post.objects.filter(
            status=1).order_by('-created_on')[:10]

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
                # To show the latest post on the post detail page.
                "latest_posts": latest_posts,
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
            comment_form.instance.user = request.user
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(request.path_info)

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


@login_required  # View for handling post likes
def post_like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

# View for handling post unlikes


class PostUnlikeView(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        return redirect('post_detail', slug=slug)

# View for user profile


@login_required
def profile(request):
    user_comments = Comment.objects.filter(user=request.user)
    context = {
        'user_comments': user_comments,
    }
    return render(request, 'profile.html', context)

# View for user settings


@login_required
def settings(request):
    return render(request, 'settings.html')

# View for editing user profile


@login_required
def edit_profile(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            if form.cleaned_data.get('remove_photo'):
                # Clear the profile photo (set it to None)
                profile.profile_photo = None
            form.save()
            # Redirect to the user's profile page or another appropriate URL
            return redirect('profile')
    else:
        form = ProfileEditForm(instance=profile)

    return render(request, 'edit_profile.html', {'form': form})

# View for editing a comment


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    # Retrieve the associated post
    post = comment.post

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()

            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'edit_comment.html', {'form': form, 'comment': comment})

# View for deleting a comment


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.user != request.user:
        raise Http404("You do not have permission to delete this comment.")

    if request.method == 'POST':
        comment.delete()

        return redirect('post_detail', slug=comment.post.slug)

    return render(request, 'delete_comment.html', {'comment': comment})
