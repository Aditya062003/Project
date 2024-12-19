from django.urls import path

from .views import (
    AllCommentsListView,
    CreateCommentView,
    CreatePostView,
    CreateUserView,
    DeletePostView,
    InfinitePostListView,
    RandomCommentListView,
    UpdatePostView,
)

urlpatterns = [
    # User endpoint
    path("users/", CreateUserView.as_view(), name="create_user"),
    # Post endpoints
    path("posts/", InfinitePostListView.as_view(), name="infinite_posts"),
    path("posts/create/", CreatePostView.as_view(), name="create_post"),
    path("posts/<uuid:post_id>/", UpdatePostView.as_view(), name="update_post"),
    path("posts/<uuid:post_id>/delete/", DeletePostView.as_view(), name="delete_post"),
    # Comment endpoints
    path(
        "posts/<uuid:post_id>/comments/",
        CreateCommentView.as_view(),
        name="create_comment",
    ),
    path(
        "posts/<uuid:post_id>/comments/all/",
        AllCommentsListView.as_view(),
        name="all_comments",
    ),
    path(
        "posts/<uuid:post_id>/comments/random/",
        RandomCommentListView.as_view(),
        name="random_comments",
    ),
]
