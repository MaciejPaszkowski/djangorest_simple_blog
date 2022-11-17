import factory.fuzzy

from authentication.models import User
from posts.models import Category, Comment, Post, PostCategories
from tests.factories_helper import create_dict_factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    # id = factory.Faker("uuid4")
    username = factory.Faker("name", locale="pl_PL")
    email = factory.Sequence(lambda n: "person{}@emailexample.com".format(n))
    password = factory.fuzzy.FuzzyText(length=20)


UserDictFactory = create_dict_factory(UserFactory)


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    # name = factory.fuzzy.FuzzyText(length=50)
    name = factory.Faker("first_name", locale="pl_PL")
    description = factory.Sequence(lambda n: "category description{}".format(n))


CategoryDictFactory = create_dict_factory(CategoryFactory)


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    id = factory.Faker("uuid4")
    author = factory.SubFactory(UserFactory)

    content = factory.Sequence(lambda n: "post content{}".format(n))
    # title = factory.fuzzy.FuzzyText(length=100)
    title = factory.Sequence(lambda n: "post title{}".format(n))

    @factory.post_generation
    def categories(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for category in extracted:
                self.category.add(category)


PostDictFactory = create_dict_factory(PostFactory)


class PostCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PostCategories

    post = factory.SubFactory(PostFactory)
    category = factory.SubFactory(CategoryFactory)


PostCategoryDictFactory = create_dict_factory(PostCategoryFactory)


class CommentPostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    post = factory.SubFactory(PostFactory)
    author = factory.SubFactory(UserFactory)
    content = factory.Sequence(lambda n: "content of comment{}".format(n))


CommentPostDictFactory = create_dict_factory(CommentPostFactory)
