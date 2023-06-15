from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
