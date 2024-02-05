from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Posters, Comment, Category


User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'poster', 'name', 'text', 'created_at',]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [ 'category']
        
        
class PosterSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Posters
        fields = ["id", "author", "title","body", "category", "created_at", "updated_at", "comments"] #
        read_only_fields = ["comments",]
        



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',)