from django.urls import path
from . import views

urlpatterns = [
    path("",views.StartingPageView.as_view(), name="starting-page"),
    path("posts", views.PostsView.as_view(), name="posts-page"),
    # Correction: original pattern used <str:slug>,
    # updated to <slug:slug> for proper URL slug handling
    path("posts/<slug:slug>", views.SinglePostView.as_view(),
         name="post-detail-page"),  # /posts/my-first-post
    path("read-later",views.ReadLaterView.as_view(), name="read-later"),
         
]
