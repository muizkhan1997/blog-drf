from django.urls import path, include
from .views import PostAPIView

urlpatterns = [
    path("blogs", PostAPIView.as_view(), name="blog_posts"),
    path("", include("likes_comments.urls"))
]
