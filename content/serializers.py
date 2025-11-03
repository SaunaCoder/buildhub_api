from rest_framework import serializers
from .models import *

class BuildSerializer(serializers.ModelSerializer):
    amount_of_likes = serializers.SerializerMethodField()
    is_liked_by_user = serializers.SerializerMethodField()

    class Meta:
        model = Build
        fields = ['id', 'name', 'description', 'author', 'lvl1to20', 'author', 'created_at', 'amount_of_likes', 'is_liked_by_user']
        read_only_fields = ['author', 'created_at', 'amount_of_likes', 'is_liked_by_user']
    
    def get_amount_of_likes(self, obj):
        return obj.likes.count()
    
    def get_is_liked_by_user(self, obj):
        return obj.likes.filter(author=self.context['request'].user).exists()

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'build', 'author']
        read_only_fields = ['author']
