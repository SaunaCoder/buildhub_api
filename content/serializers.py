from rest_framework import serializers
from .models import *

class BuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Build
        fields = ['id', 'name', 'description', 'author', 'lvl1to20', 'author', 'created_at']
        read_only_fields = ['author', 'created_at']