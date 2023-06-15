from likes_comments.serializers import CommentSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from posts.models import Post

class CommentPostView(APIView):
    def post(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        data = {"user": request.data['user'], "post": post.id, "content": request.data['content']}
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
