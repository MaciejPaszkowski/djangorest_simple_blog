import pytest
from django.core.exceptions import ValidationError

from tests.factories import PostFactory, UserFactory


class TestModels:
    pytestmark = pytest.mark.django_db

    def setup_method(self, method):
        self.Post = PostFactory.create()

    def test_post_create(self):
        user = UserFactory.create()
        post = PostFactory.create(author=user)

        assert post.pk is not None
        assert post.author.id == user.id
        assert post.author.username == user.username
        assert post.author.email == user.email

        assert post.title is not None
        assert post.content is not None
        assert post.created_at is not None

    def test_user_create(self):

        user = UserFactory.create()
        assert user.pk is not None
        assert user.email is not None
        assert user.password is not None
