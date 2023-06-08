# pylint: disable=missing-module-docstring
from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """
    This class serializes Client model.
    """
    class Meta:
        model = Post
        fields = "__all__"
