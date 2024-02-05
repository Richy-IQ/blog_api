from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from datetime import datetime, timedelta
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from . models import Posters, Comment
from . permissions import IsReadOnlyOrUnauthenticated, AllowUnauthenticatedComment, IsAuthorPermission
from . serializers import PosterSerializer, CommentSerializer, UserSerializer
from django.utils import timezone


User = get_user_model()


class PostersList(generics.ListCreateAPIView):
    permission_classes = [IsReadOnlyOrUnauthenticated]
    queryset = Posters.objects.all()
    serializer_class = PosterSerializer

    def get_queryset(self):
        days = int(self.request.GET.get("days", 7))
        all_posts = Posters.objects.all()
        if 'recent' in self.request.GET:
           seven_days_ago = timezone.now() - timedelta(days=days)
           all_posts = all_posts.filter(created_at__gte=seven_days_ago)
        return all_posts


class PostersDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsReadOnlyOrUnauthenticated ]#IsAuthorPermission
    queryset = Posters.objects.all()
    serializer_class = PosterSerializer

    def perform_update(self, serializer):
            # print(self.get_object().author == self.request.user, self.get_object().author, self.request.user)
        if not (self.get_object().author == self.request.user):
            raise ValueError("you can't perform this operation")
        serializer.save(author=self.request.user)

    def perform_destroy(self, serializer):
        if not (self.get_object().author == self.request.user):
             raise ValueError("you cant delete")
        serializer.save(author=self.request.user)


class CommentListCreateView(generics.ListCreateAPIView):
    permission_classes = [AllowUnauthenticatedComment,]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowUnauthenticatedComment,]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class PostViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsReadOnlyOrUnauthenticated]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsAdminUser]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
