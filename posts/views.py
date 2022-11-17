from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response

from posts.models import Category
from posts.serializers import CategorySerializer

User = get_user_model

# Create your views here.
class HelloPostView(generics.GenericAPIView):
    def get(self, request):
        return Response(data={"message": "Hello Post"}, status=status.HTTP_200_OK)


class CategoryView(generics.GenericAPIView):
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
