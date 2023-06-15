from likes_comments.serializers import LikeSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from posts.models import Post
from rest_framework.views import APIView
from rest_framework import status

class LikePostView(APIView):
    def post(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        data = {"user": request.data['user'], "post": post.id}
        serializer = LikeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
