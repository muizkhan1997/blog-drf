from django.urls import path
from likes_comments.views import LikePostView, CommentPostView

urlpatterns = [
    path('posts/<int:post_id>/likes/', LikePostView.as_view(), name='like_post'),
    path('posts/<int:post_id>/comments/', CommentPostView.as_view(), name='comment_post'),
]
