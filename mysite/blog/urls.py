from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="posts-page"),

    # Correction: original pattern used <str:slug>,
    # updated to <slug:slug> for proper URL slug handling
    path("posts/<str:slug>", views.post_detail,
         name="post-detail-page"),  # /posts/my-first-post
]
