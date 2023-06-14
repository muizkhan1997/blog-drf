from django.db import models
from django.contrib.auth.models import User
from likes_comments.models import Like, Comment

class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=128, null=True)
    likes = models.ManyToManyField(User, through=Like, related_name='liked_posts')
    comments = models.ManyToManyField(User, through=Comment, related_name='commented_posts')

    def __str__(self) -> str:
        return f"{self.title}"
