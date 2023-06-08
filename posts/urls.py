from django.urls import path
from .views import PostAPIView

urlpatterns = [
    path("blogs", PostAPIView.as_view(), name="blog_posts"),
]
