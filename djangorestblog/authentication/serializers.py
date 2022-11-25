import uuid

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from posts.models import Category, Comment, Post, PostCategories
from rest_framework import serializers, status
from rest_framework.validators import ValidationError

User = get_user_model()


class UserCreationSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(min_length=8)
    id = uuid.uuid4()

    class Meta:
        model = User
        fields = ["username", "email", "id", "password"]
        read_only_fields = ["email", "username", "id"]
        write_only_fields = ["password"]

    def validate(self, attrs):
        username_exists = User.objects.filter(username=attrs["username"]).exists()
        email_exits = User.objects.filter(email=attrs["email"]).exists()
        print("walidacja")

        if username_exists or email_exits:
            raise ValidationError(
                detail="User with username or email exists",
                code=status.HTTP_403_FORBIDDEN,
            )

        return super().validate(attrs)

    def create(self, validated_data):
        new_user = User(**validated_data)
        print(new_user)
        new_user.password = make_password(validated_data.get("password"))
        print(new_user.password)
        # new_user.id=uuid.uuid4()
        print(new_user)
        new_user.save()

        return new_user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email")
        read_only_fields = ("email", "username")


class UserSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "id")
        read_only_fields = ("username", "id")
