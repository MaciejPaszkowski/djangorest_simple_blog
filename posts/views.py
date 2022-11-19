from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from posts.models import Category, Post
from posts.serializers import (CategorySerializer, PostCategoriesSerializer,
                               PostSerializer, PostWriteSerializer)

User = get_user_model

# Create your views here.
class HelloPostView(generics.GenericAPIView):
    def get(self, request):
        return Response(data={"message": "Hello Post"}, status=status.HTTP_200_OK)


class CategoryView(generics.GenericAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request):
        categories = Category.objects.all()
        serializer = self.serializer_class(instance=categories, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

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


class PostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    authentication_classes = [JWTAuthentication]
    queryset = Post.objects.all()

    def get(self, request):
        posts = Post.objects.all()
        serializer = self.serializer_class(instance=posts, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

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

        if "content" and "title" in data:

            data2 = {
                "title": data["title"],
                "content": data["content"],
                "author_id": user.id,
            }

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
                            category_pre = Category.objects.filter(
                                name=category
                            ).first()

                        if category_pre:
                            self._serialize_category(
                                serializer_data=serializer.data,
                                category_pre=category_pre,
                            )
                            category_pre = None

                return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
