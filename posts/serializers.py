# pylint: disable=missing-module-docstring
from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    """
    This class serializes Post model.
    """

    class Meta:
        model = Post
        fields = "__all__"

    def create(self, validated_data):
        return Post.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.content = validated_data.get("title", instance.title)
        instance.title = validated_data.get("content", instance.content)
        return instance

class PostDetailedSerializer(serializers.ModelSerializer):
    """
    This class serializes Post model.
    """

    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ("id", "title", "content", "author")

    def to_representation(self, instance):
        response_dict = super().to_representation(instance)
        return response_dict["title"]      
