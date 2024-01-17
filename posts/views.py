from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from datetime import datetime, timedelta
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from . models import Post, Comment
from . permissions import IsReadOnlyOrUnauthenticated
from . serializers import PostSerializer, CommentSerializer, UserSerializer
from django.utils import timezone


class PostList(generics.ListCreateAPIView):
    permission_classes = [IsReadOnlyOrUnauthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


    def get_queryset(self):
        seven_days_ago = timezone.now() - timedelta(days=7)
        return Post.objects.filter(created_at__gte=seven_days_ago)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsReadOnlyOrUnauthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_update(self, serializer):
            # print(self.get_object().author == self.request.user, self.get_object().author, self.request.user)
        if not (self.get_object().author == self.request.user):
            raise ValueError("you can't perform this operation")
        return super().perform_update(serializer)

    

    def perform_destroy(self, serializer):
        if not (self.get_object().author == self.request.user):
             raise ValueError("you cant delete")
        return super().perform_destroy(serializer)


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class UserList(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsReadOnlyOrUnauthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
