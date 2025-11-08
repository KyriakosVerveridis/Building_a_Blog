from datetime import date
from django.shortcuts import render
from .models import Post

all_posts = [
  
]

def get_date(post):
    """Get the date from the given post dictionary"""
    return post["date"]

# Create your views here.


def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    # sorted_posts = sorted(all_posts, key=get_date)
    # latest_posts = sorted_posts[-3:]

    """
    Context dictionary for the template: contains the 3 
    most recent posts to display on the index.html template.
    """
    context = {
        "posts": latest_posts
    }

    """Render the starting (home) page of the blog."""
    return render(request, "blog/index.html", context)

def posts(request):
    """
    Context dictionary for the template: contains all
    blog posts to display on the all_posts.html template
    """
    context = {
        "all_posts": all_posts
    }

    """Display a list of all blog posts."""
    return render(request, "blog/all-posts.html", context)

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post["slug"] == slug)

    """
    Context dictionary for the template: contains
    blog post to display on the post-detail.html template.
    """
    context = {
        "post": identified_post
    }
    
    """Show the details for a single blog post."""
    return render(request, "blog/post-detail.html", context)
