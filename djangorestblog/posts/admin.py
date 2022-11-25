from django.contrib import admin

from .models import Category, Comment, Post, PostCategories

# Register your models here


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # list_display = ["author", "title", "content", "categories"]
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]


@admin.register(PostCategories)
class PostCategoriesAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
