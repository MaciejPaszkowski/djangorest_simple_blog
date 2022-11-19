import pytest
from django.core.exceptions import ValidationError

from posts.models import Category, Comment, PostCategories
from tests.factories import (CategoryFactory, CommentPostFactory,
                             PostCategoryFactory, PostFactory, UserFactory)


class TestModels:
    pytestmark = pytest.mark.django_db

    def setup_method(self, method):
        # self.post = PostFactory.create()
        # self.category
        pass

    def test_post_create_with_categories(self):
        user = UserFactory.create()

        categories = CategoryFactory.create_batch(3)
        category = CategoryFactory.create()
        post = PostFactory.create(author=user)
        post2 = PostFactory(author=user)

        postcategory = PostCategoryFactory(category=category, post=post2)

        for zz in categories:

            postcategories = PostCategoryFactory(category=zz, post=post)

        assert post.pk is not None
        assert post.author == user
        assert post.author.username == user.username
        assert post.author.email == user.email

        assert post.title is not None
        assert post.content is not None
        assert post.created_at is not None

        # for zz in post.categories.all():
        #     print(zz)             # <== how to look to many categories in post ;)

        assert category.name is not None
        assert post.categories.count() == 3
        assert post2.categories.count() == 1

    def test_post_create_with_categories2(self):
        user = UserFactory.create()

        categories = CategoryFactory.create_batch(3)
        category = CategoryFactory.create()
        post = PostFactory.create(author=user)
        post2 = PostFactory(author=user)
        post3 = PostFactory(author=user)
        post3.categories.add(category)
        print(post3)

        postcategory = PostCategoryFactory(category=category, post=post2)

        for zz in categories:

            postcategories = PostCategoryFactory(category=zz, post=post)

        assert post.pk is not None
        assert post.author == user
        assert post.author.username == user.username
        assert post.author.email == user.email

        assert post.title is not None
        assert post.content is not None
        assert post.created_at is not None

        # for zz in post.categories.all():
        #      print(zz)
        #      print(zz.id)
        #      print(zz.name)
        #      print(zz.description)             # <== how to look to many categories in post ;)

        assert category.name is not None
        assert post.categories.count() == 3
        assert post2.categories.count() == 1

        # assert 0==1

    def test_user_create(self):

        user = UserFactory.create()
        assert user.pk is not None
        assert user.email is not None
        assert user.password is not None

    def test_category_with_posts(self):
        user = UserFactory.create()
        category = CategoryFactory.create()
        category2 = CategoryFactory.create()
        posts = PostFactory.create_batch(3)
        posts2 = PostFactory.create_batch(3)
        # for post in posts:
        #     print(post)
        for zz in posts:

            postcategories = PostCategoryFactory(category=category, post=zz)

        for zz in posts2:
            print(zz)
            postcategories = PostCategoryFactory(category=category2, post=zz)

        postCategories = PostCategoryFactory(category=category, post=posts2[0])

        # for zz in posts:
        #     print(zz)
        #     print(zz.category)
        #     tt=zz.categories.all()
        #     for vv in tt:
        #         print(vv)

        # tt=PostCategories.objects.all()

        # for xx in tt:
        #     print("==>>",xx.category," >>", xx.post)

        # normal many_to_many access :

        post_has_two_categories = PostCategories.objects.filter(post=posts2[0])
        category_has_many_post = PostCategories.objects.filter(category=category)

        # print(post_has_two_categories)

        # print("**************")
        # print(category_has_many_post)
        # print(category.name)
        # print(category.post_categories.all())

        assert post_has_two_categories[0].category == category2
        assert post_has_two_categories[1].category == category

        assert category_has_many_post[0].category == category
        assert category_has_many_post[1].category == category
        assert category_has_many_post[2].category == category
        assert category_has_many_post[3].category == category

        assert category.post_categories.count() == 4
        """
        3 from posts , 1 from posts2  , we have access to all post in "category " via .post_categories  field ,
        and after .all() we have list of these posts

        """
        assert category.post_categories.all() is not []

        assert category.name is not None
        # assert category.name==''

    def test__add_comment_to_post(self):
        user = UserFactory.create()
        user2 = UserFactory.create()
        category = CategoryFactory.create()
        post = PostFactory.create(author=user)

        postCategories = PostCategoryFactory(category=category, post=post)

        comment = CommentPostFactory(post=post, author=user)
        comment2 = CommentPostFactory.create()
        comment3 = CommentPostFactory(post=post, author=user2)

        #  print(user)
        #  print(user2)
        #  print(comment.author)
        #  print(comment)
        #  print(comment2)
        #  print(comment3)

        assert comment.content is not None

        post_has_comments = Comment.objects.filter(post=post)
        print(post_has_comments[0].author)
        print(user)
        assert post_has_comments[0].author.email == user.email
        assert post_has_comments[1].author.email == user2.email

    #  assert comment.content ==''
