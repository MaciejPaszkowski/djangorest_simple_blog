from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response


# Create your views here.
class HelloPostView(generics.GenericAPIView):
    def get(self, request):
        return Response(data={"message": "Hello Post"}, status=status.HTTP_200_OK)
