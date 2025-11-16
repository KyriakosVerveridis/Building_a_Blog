from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView

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


class SinglePostView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post # Uses the Post model.

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        # Adds the CommentForm fields to the context.
        context["comment_form"] = CommentForm()
        return context
    