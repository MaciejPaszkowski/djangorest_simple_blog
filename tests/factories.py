import factory.fuzzy

from authentication.models import User
from posts.models import Category, Post, PostCategories


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name", locale="pl_PL")
    email = factory.Sequence(lambda n: "person{}@emailexample.com".format(n))
    password = factory.fuzzy.FuzzyText(length=20)


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.fuzzy.FuzzyText(length=50)
    discription = factory.fuzzy.FuzzyText(length=100)


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    author = factory.SubFactory(UserFactory)
    content = factory.fuzzy.FuzzyText(length=1000)
    title = factory.fuzzy.FuzzyText(length=100)

    # @factory.post_generation
    # def categories(self,create, extracted, **kwargs):
    #     if not create:
    #         return
    #     if extracted:
    #         for category in extracted:
    #             self.category.add(category)


class PostCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PostCategories

    post = factory.SubFactory(PostFactory)
    category = factory.SubFactory(CategoryFactory)
