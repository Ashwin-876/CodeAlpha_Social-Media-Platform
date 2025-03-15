from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing posts.
    - Users can create, retrieve, update, and delete their own posts.
    - Lists all posts ordered by creation time.
    """
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing comments on posts.
    - Users can add comments to posts.
    - Allows listing all comments related to a post.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LikeViewSet(viewsets.ViewSet):
    """
    ViewSet for handling likes.
    - Users can like/unlike posts.
    - Prevents duplicate likes.
    """
    permission_classes = [IsAuthenticated]

    def create(self, request):
        post_id = request.data.get('post')
        post = Post.objects.get(id=post_id)
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            like.delete()  # Unlike the post if already liked
            return Response({"message": "Post unliked"}, status=status.HTTP_204_NO_CONTENT)
        
        return Response({"message": "Post liked"}, status=status.HTTP_201_CREATED)
