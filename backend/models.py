from django.contrib.auth.models import User # type: ignore
from django.db import models # type: ignore

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who created the post
    content = models.TextField()  # Post content
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return f"{self.user.username} - {self.content[:30]}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")  # Related post
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who commented
    content = models.TextField()  # Comment text
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return f"{self.user.username} on {self.post.id}"

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")  # Related post
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who liked the post

    class Meta:
        unique_together = ('post', 'user')  # Prevent duplicate likes

    def __str__(self):
        return f"{self.user.username} liked {self.post.id}"
