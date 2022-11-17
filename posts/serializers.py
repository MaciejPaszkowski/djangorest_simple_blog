from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers, status
from rest_framework.validators import ValidationError

from authentication.serializers import UserSerializer
from posts.models import Category, Comment, Post, PostCategories

User = get_user_model()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=User.objects.all(), source="author"
    )

    class Meta:
        model = Post
        fields = ("author", "title", "content", "author_id")


class PostCategoriesSerializer(serializers.ModelSerializer):
    post = PostSerializer(read_only=True)
    post_id = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Post.objects.all(), source="post"
    )

    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Category.objects.all(), source="category"
    )

    class Meta:
        model = PostCategories
        fields = "__all__"


class CommentSerailizer(serializers.ModelSerializer):
    # post=PostSerializer()
    post_id = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Post.objects.all(), source="post"
    )
    # author=UserSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=User.objects.all(), source="author"
    )

    class Meta:
        model = Comment
        fields = ["post_id", "author_id", "content"]
