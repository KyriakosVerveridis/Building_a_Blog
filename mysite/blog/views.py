from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.views import View


from .models import Post
from .forms import CommentForm


# Create your views here.


class StartingPageView(ListView):
    """
    Displays the 3 most recent blog posts on the homepage.
    Uses Django's ListView to automatically load Post objects
    and render them into the index template.
    """
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        """
        Override the default queryset to return only
        the latest three posts ordered by date (descending).
        """
        queryset =  super().get_queryset() # Get all posts based on the model
        data = queryset[:3] # Select only the most recent 3
        return data


class PostsView(ListView):
    """
    Displays all blog posts ordered from newest to oldest.
    Uses Django's ListView to automatically retrieve Post objects
    and render them in the 'all-posts' template.
    """
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]  # Νewest ones appear first
    context_object_name = "all_posts"


class SinglePostView(View):
    """
    Handles displaying a single blog post (GET) and processing new comments (POST)
    """
    def get(self, request, slug):
        # Retrieve the requested post using its slug.
        post = Post.objects.get(slug=slug) 
        context = {
            "post": post,
            "post_tags":post.tags.all(),  # Load all tags related to the post
            "comment_form":CommentForm() # Provide a blank form for new comments
        }
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):
        # Bind submitted data to the comment form
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug) 

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            # Redirect to the same post page (PRG pattern: POST → Redirect → GET)
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
        
        context = {
            "post": post,
            "post_tags":post.tags.all(),
            "comment_form": comment_form # Re-render the invalid form (with errors)
        }
        return render(request, "blog/post-detail.html", context)

    