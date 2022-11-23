from django.urls import path

from . import views

urlpatterns = [
    path("", views.HelloPostView.as_view(), name="hello_post"),
    path("categories/", views.CategoryView.as_view(), name="categories"),
    path("categories/<uuid:id>/", views.CategoryIdView.as_view(), name="category"),
    path("posts/", views.PostView.as_view(), name="posts"),
    path("posts/<uuid:id>/", views.PostIdView.as_view(), name="post"),
    path(
        "posts/<uuid:id>/comments/", views.CommentByPost.as_view(), name="post_comments"
    ),
    path(
        "posts/category/<str:name_id>/",
        views.PostByCategory.as_view(),
        name="category_posts",
    ),
    path("comments/", views.CommentView.as_view(), name="comments"),
    path("comments/<uuid:id>/", views.CommentIdView.as_view(), name="comment"),
    path("authors/<int:id>/posts/", views.PostByUser.as_view(), name="author_posts")
    # path("onlycomments/", views.CommentOnlyView.as_view(), name="only_comment"),
]
