from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100, null=False)
    discription = models.CharField(max_length=200)

    def _str_(self):
        return f"<Category {self.name}"


class Post(models.Model):
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
