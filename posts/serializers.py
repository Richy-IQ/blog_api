from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post, Comment




class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'name', 'text', 'created_at',]

        
class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ["id", "author", "title","body", "created_at", "comments"]
        read_only_fields = ["comments"]



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)