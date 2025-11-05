from rest_framework import serializers
from .models import *

class BuildSerializer(serializers.ModelSerializer):
    amount_of_likes = serializers.SerializerMethodField()
    is_liked_by_user = serializers.SerializerMethodField()
    is_user_an_author = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Build
        fields = ['id', 'name', 'description', 'lvl1to20', 'author', 'created_at', 'amount_of_likes', 'is_liked_by_user', 'is_user_an_author', 'comments']
        read_only_fields = ['author', 'created_at', 'amount_of_likes', 'is_liked_by_user', 'is_user_an_author', 'comments']
    
    def get_amount_of_likes(self, obj):
        return obj.likes.count()
    
    def get_is_liked_by_user(self, obj):
        return obj.likes.filter(author=self.context['request'].user).exists()
    
    def get_comments(self, obj):
        return CommentSerializer(obj.comments.all(), many = True).data
    
    def get_is_user_an_author(self, obj):
        return obj.author == self.context['request'].user

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'build', 'author']
        read_only_fields = ['author']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'build', 'parent', 'author', 'text', 'created_at']
        read_only_fields = ['author', 'created_at']

    def validate(self, data):
        if not data.get('build') and not data.get('parent'):
            raise serializers.ValidationError("Comment must have either build or parent")
        return data

