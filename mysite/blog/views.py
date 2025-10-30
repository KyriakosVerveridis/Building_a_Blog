from django.shortcuts import render

# Create your views here.

def starting_page(request):
  """Render the starting (home) page of the blog."""
  return render(request,"blog/index.html")

def posts(request):
  """Display a list of all blog posts."""
  return render(request,"blog/all-posts.html")

def post_detail(request):
  """Show the details for a single blog post."""
  pass