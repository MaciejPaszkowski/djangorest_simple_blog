import pytest

from posts.models import Comment, PostCategories
from posts.serializers import (CategorySerializer, CommentSerailizer,
                               PostCategoriesSerializer, PostSerializer)
from tests.factories import (CategoryDictFactory, CategoryFactory,
                             CommentPostDictFactory, CommentPostFactory,
                             PostCategoryDictFactory, PostCategoryFactory,
                             PostDictFactory, PostFactory, UserFactory)


class TestSerializers:

    pytestmark = pytest.mark.django_db

    def test_posts_create_serializer(self):
        data = PostDictFactory()

        user = UserFactory()
        print(user.id)

        data["author_id"] = user.id

        seralizer = PostSerializer(data=data)

        seralizer.is_valid(raise_exception=True)
        seralizer.save()
        # assert 0==1

    def test_category_create_serailizer(self):
        data = CategoryDictFactory()
        serializer = CategorySerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    def test_post_has_category_serializer(self):
        data = PostCategoryDictFactory()

        user = UserFactory()
        category = CategoryFactory()
        post = PostFactory(author=user)

        postcategories = PostCategories(post=post, category=category)
        data["post_id"] = post.id
        data["category_id"] = category.id

        serializer = PostCategoriesSerializer(data=data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        # assert 0==1

    def test_post_has_comments_serializer(self):

        data = CommentPostDictFactory()
        print(data)

        user = UserFactory()
        user2 = UserFactory()

        post = PostFactory(author=user)
        comment1 = CommentPostFactory(post=post, author=user2)
        comment2 = CommentPostFactory(post=post, author=user)

        # print(comment1)
        # print(comment2)

        post2 = PostFactory(author=user)
        comment3 = CommentPostFactory(post=post2, author=user)

        data["post_id"] = post.id

        data["author_id"] = user.id

        del data["post"]
        del data["author"]
        # print("____________________")
        # print(data)

        serializer = CommentSerailizer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        post_has_comments = Comment.objects.filter(post=post)
        post2_has_no_comments = Comment.objects.filter(post=post2)
        # print("@@@@@")
        # print(post_has_comments)
        # print(post2_has_no_comments)

        # for xx in post_has_comments:
        #     print(xx.author)
        #     print(xx.post)
        #     print(xx.content)
        # print(len(post_has_comments))

        assert (len(post_has_comments)) == 3  # yes 3 , first from dictfactory
        assert (len(post2_has_no_comments)) == 1
