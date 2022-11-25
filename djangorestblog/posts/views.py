from authentication.models import User
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters
from posts.filters import CategoryFilter, CommentFilter, PostFilter
from posts.models import Category, Comment, Post, PostCategories
from posts.serializers import (CategorySerializer, CommentReadSerializer,
                               CommentWriteNoAuthorSerializer,
                               CommentWriteSerializer,
                               PostCategoriesSerializer, PostSerializer,
                               PostSmallSerializer, PostWriteSerializer)
from rest_framework import generics, status, viewsets
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

# User = get_user_model

# Create your views here.
class HelloPostView(generics.GenericAPIView):
    def get(self, request):
        return Response(data={"message": "Hello Post"}, status=status.HTTP_200_OK)


class CategoryView(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CategoryFilter

    # @swagger_auto_schema(operation_summary="Create a post")
    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryIdView(generics.GenericAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    authentication_classes = [JWTAuthentication]

    def get(self, request, id):

        category = get_object_or_404(Category, pk=id)
        serializer = self.serializer_class(instance=category)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):

        category = get_object_or_404(Category, pk=id)
        serializer = self.serializer_class(instance=category, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        category = get_object_or_404(Category, pk=id)

        category.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class PostView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    authentication_classes = [JWTAuthentication]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PostFilter

    queryset = Post.objects.all()

    def _serialize_category(self, serializer_data, category_pre):
        data = {}
        data["post_id"] = serializer_data["id"]
        data["category_id"] = category_pre.id
        serializer_category = PostCategoriesSerializer(data=data)
        if serializer_category.is_valid():
            serializer_category.save()

    def post(self, request, *args, **kwargs):
        data = request.data
        user = request.user
        print(data)

        if "content" in data.keys() and "title" in data.keys():

            data2 = {
                "title": data["title"],
                "content": data["content"],
                "author_id": user.id,
            }
        else:
            data2 = {}

        serializer = PostWriteSerializer(data=data2)

        if serializer.is_valid():
            serializer.save()

            if "categories" in data:

                data2["categories"] = data["categories"]
                category_pre = None

                for category in data["categories"]:
                    if isinstance(category, dict):
                        category_pre = Category.objects.filter(
                            name=category["name"]
                        ).first()
                    elif isinstance(category, str):
                        print("category:", category)
                        category_pre = Category.objects.filter(name=category).first()

                    if category_pre:
                        self._serialize_category(
                            serializer_data=serializer.data,
                            category_pre=category_pre,
                        )
                        category_pre = None

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostIdView(generics.GenericAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    authentication_classes = [JWTAuthentication]

    def _serialize_category(self, serializer_data, category_pre):
        data = {}
        data["post_id"] = serializer_data["id"]
        data["category_id"] = category_pre.id
        serializer_category = PostCategoriesSerializer(data=data)
        if serializer_category.is_valid():
            serializer_category.save()

    def get(self, request, id):
        post = get_object_or_404(Post, pk=id)
        serializer = self.serializer_class(instance=post)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):  # changes of category at this moment is not implemented
        data = request.data
        user = request.user

        if "content" in data.keys() and "title" in data.keys():

            data2 = {
                "title": data["title"],
                "content": data["content"],
                "author_id": user.id,
                "id": id,
            }
        else:
            data2 = {}

        post = get_object_or_404(Post, pk=id)
        serializer = PostWriteSerializer(instance=post, data=data2)

        if (
            serializer.is_valid() and post.author_id == user.id
        ):  # another user cannot change
            serializer.save()

            if "categories" in data:

                data2["categories"] = data["categories"]
                category_pre = None

                for category in data["categories"]:
                    if isinstance(category, dict):
                        category_pre = Category.objects.filter(
                            name=category["name"]
                        ).first()
                    elif isinstance(category, str):
                        print("category:", category)
                        category_pre = Category.objects.filter(name=category).first()

                    if category_pre:
                        self._serialize_category(
                            serializer_data=serializer.data,
                            category_pre=category_pre,
                        )
                        category_pre = None

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):

        user = request.user

        post = get_object_or_404(Post, pk=id)
        if post.author_id == user.id:

            post.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
        data = {"message": "You are not the author of this post"}
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


class CommentView(generics.ListCreateAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]
    queryset = Comment.objects.all()
    serializer_class = CommentReadSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CommentFilter

    def post(self, request):
        data = request.data
        user = request.user
        print(user)
        print(data)

        if "post_id" in data.keys() and "content" in data.keys():

            data2 = {
                "post_id": data["post_id"],
                "content": data["content"],
            }

        else:
            data2 = {}

        if user.id:
            data2["author_id"] = user.id
            serializer = CommentWriteSerializer(data=data2)

        else:
            data2["author_id"] = None
            serializer = CommentWriteNoAuthorSerializer(data=data2)

        if serializer.is_valid():
            serializer.save()
            print(serializer.data)

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentOnlyView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentReadSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CommentFilter


class CommentIdView(generics.GenericAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CommentWriteSerializer
    authentication_classes = [JWTAuthentication]

    def get(self, request, id):
        comment = get_object_or_404(Comment, pk=id)
        serializer = CommentReadSerializer(instance=comment)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):  # changes of category at this moment is not implemented
        data = request.data
        user = request.user

        if "content" in data.keys() and "post_id" in data.keys():

            data2 = {
                "content": data["content"],
                "author_id": user.id,
                "post_id": data["post_id"],
                "id": id,
            }
        else:
            data2 = {}

        comment = get_object_or_404(Comment, pk=id)

        serializer = self.serializer_class(instance=comment, data=data2)

        if (
            serializer.is_valid() and comment.author_id == user.id
        ):  # another user cannot change
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):

        user = request.user

        comment = get_object_or_404(Comment, pk=id)
        if comment.author_id == user.id:

            comment.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)
        data = {"message": "You are not the author of this comment"}
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


class CommentByPost(generics.GenericAPIView):
    serializer_class = CommentReadSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # authentication_classes = [JWTAuthentication]

    def get(self, request, id):

        post = get_object_or_404(Post, pk=id)

        comments = Comment.objects.filter(post=post)

        serializer = self.serializer_class(instance=comments, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class PostByUser(generics.GenericAPIView):
    serializer_class = PostSmallSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    # authentication_classes = [JWTAuthentication]

    # def get_queryset(self):
    #     user = get_object_or_404(User, pk=id)

    #     return Post.objects.filter(author=user)
    queryset = []

    def get(self, request, id):  # user id (int)

        user = get_object_or_404(User, pk=str(id))

        posts = Post.objects.filter(author=user)

        serializer = self.serializer_class(instance=posts, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class PostByCategory(generics.GenericAPIView):
    serializer_class = PostSmallSerializer
    queryset = []

    def get(self, request, name_id):

        # posts=[]

        category = get_object_or_404(Category, name=name_id)

        # postcategory=PostCategories.objects.filter(category=category)

        # for post in postcategory:
        #     posts.append(post.post)

        category_posts = category.post_categories.all()
        print(category_posts)
        serializer = self.serializer_class(instance=category_posts, many=True)
        # serializer = self.serializer_class(instance=posts, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
