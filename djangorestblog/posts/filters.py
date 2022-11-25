import django_filters
from posts.models import Category, Comment, Post


class PostFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = {
            "title": [
                "icontains",
            ],
            "content": [
                "icontains",
            ],
        }


class CommentFilter(django_filters.FilterSet):
    class Meta:
        model = Comment
        fields = {
            "content": [
                "icontains",
            ]
        }


class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = {
            "name": [
                "icontains",
            ],
            "description": [
                "icontains",
            ],
        }
