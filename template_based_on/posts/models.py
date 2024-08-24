from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=225)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=225)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    picture = models.ImageField()
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_recommended = models.BooleanField(default=False)  # Поле для рекомендаций

    def __str__(self):
        return self.title

class PostAuthor(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

class Comment(models.Model):
    posts = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    body = models.TextField(default='')
    created_time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return f"Comment - {self.body} by {self.user}"