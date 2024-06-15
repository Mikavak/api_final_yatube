from django.shortcuts import get_object_or_404
from rest_framework import filters, generics, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Comment, Group, Post
from .permissions import IsOwnerOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class FollowViewSet(generics.ListCreateAPIView):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.user.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        IsOwnerOrReadOnly]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [
        permissions.AllowAny]


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        get_object_or_404(Post, id=self.kwargs.get("post_id"))
        serializer.save(
            author=self.request.user,
            post_id=self.kwargs.get("post_id"))

    def get_queryset(self):
        return get_object_or_404(
            Post,
            id=self.kwargs.get("post_id")
        ).comments
