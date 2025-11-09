from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.


def starting_page(request):
    """
    View for the blog's home page.
    Retrieves the 3 most recent Post objects from the database
    (managed through the Django admin) and renders them in the index template.
    """
    latest_posts = Post.objects.all().order_by("-date")[:3] # Get the 3 latest posts
    context = {
        "posts": latest_posts
    }
    return render(request, "blog/index.html", context)


def posts(request):
    """
    View for displaying all blog posts.
    Retrieves all Post objects from the database (managed via Django admin)
    and renders them in the all-posts template.
    """
    all_posts = Post.objects.all().order_by("-date") # Get all latest posts from newest
    context = {
        "all_posts": all_posts
    }
    return render(request, "blog/all-posts.html", context)


def post_detail(request, slug):
    """
    Context dictionary for the template: contains
    blog post to display on the post-detail.html template.
    """
    identified_post = get_object_or_404(Post, slug=slug) # Get the post by slug or return 404 if not found 
    context = {
        "post": identified_post,
        "post_tags":identified_post.tags.all() # Get all tags associated with the post
    }
    """Show the details for a single blog post."""
    return render(request, "blog/post-detail.html", context)
