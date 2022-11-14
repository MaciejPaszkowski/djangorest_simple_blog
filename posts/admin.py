from django.contrib import admin

from .models import Category, Post, PostCategories

# Register your models here


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["author", "title", "content"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "discription"]


@admin.register(PostCategories)
class PostCategories(admin.ModelAdmin):
    pass
