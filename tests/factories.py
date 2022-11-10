import factory.fuzzy

from authentication.models import User
from posts.models import Post


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name", locale="pl_PL")
    email = factory.Sequence(lambda n: "person{}@emailexample.com".format(n))
    password = factory.fuzzy.FuzzyText(length=20)


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    author = factory.SubFactory(UserFactory)
    content = factory.fuzzy.FuzzyText(length=1000)
    title = factory.fuzzy.FuzzyText(length=100)


# author = models.ForeignKey(User, on_delete=models.CASCADE)
#     title=models.CharField(max_length=100)
#     content= models.CharField(max_length=1000)
#     created_at=models.DateTimeField(auto_now_add=True)
