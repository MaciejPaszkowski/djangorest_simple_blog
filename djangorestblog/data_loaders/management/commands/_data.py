import os
import sys

working_dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(working_dir_path, "../../../../djangorestblog"))

from authentication.models import User
from data_loaders.values_dict import (CATEGORIES, COMMENTS, POST_CATEGORIES,
                                      POSTS, USERS)
from posts.models import Category, Comment, Post, PostCategories

print(working_dir_path)


def load_users():
    for user in USERS:
        User.objects.get_or_create(
            username=user["username"], email=user["email"], password=user["password"]
        )


def load_categories():
    for category in CATEGORIES:
        Category.objects.get_or_create(
            name=category["name"], description=category["description"]
        )


def load_posts():
    for post in POSTS:
        author = User.objects.get(username=post["author"])
        Post.objects.get_or_create(
            id=post["id"], title=post["title"], content=post["content"], author=author
        )


def load_post_categories():
    for post_categories in POST_CATEGORIES:
        post = Post.objects.get(id=post_categories["post_id"])
        for categories in post_categories["categories"]:
            category = Category.objects.get(name=categories)
            PostCategories.objects.get_or_create(post=post, category=category)


def load_comments():
    for comment in COMMENTS:
        post = Post.objects.get(id=comment["post_id"])
        author = User.objects.filter(
            username=comment["author"]
        ).first()  # because we have author=null
        Comment.objects.get_or_create(
            post=post, content=comment["content"], author=author
        )


def seed_blog():
    loaders = [
        ("Loading users", load_users),
        ("Loading categories", load_categories),
        ("Loading posts", load_posts),
        ("Loading post_categories", load_post_categories),
        ("Loading comments", load_comments),
    ]

    max = len(loaders)
    for i, (msg, f) in enumerate(loaders, start=1):
        print("Step {} of {}: {}".format(i, max, msg))
        f()
    print("Loaded all mvp data")
