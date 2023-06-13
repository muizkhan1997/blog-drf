from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import PostSerializer, PostDetailedSerializer
from .models import Post
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

class PostAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostDetailedSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            raise ValidationError(serializer.errors)
    