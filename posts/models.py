import uuid

from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()


class ModelId(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self) -> str:
        return self.id


class Category(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=False)
    discription = models.CharField(max_length=200)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"<Category {self.name}"


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=100, null=False)
    content = models.CharField(max_length=1000, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(
        Category, related_name="post_categories", through="PostCategories"
    )

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"<Post {self.author}:{self.title}"


class PostCategories(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return f"<PostCategories {self.post.title} / {self.category.name}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    content = models.CharField(max_length=1000, null=False)

    def __str__(self):
        return f"<Comment {self.post.title} / {self.content}"
