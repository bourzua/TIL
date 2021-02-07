from rest_framework import serializers
from .models import Community, Comment
from accounts.serializers import UserSerializer

class CommunitySerializer(serializers.ModelSerializer):
    
    user = UserSerializer(read_only=True)

    class Meta:
        model = Community
        fields = ('id', 'user', 'title', 'content', 'created_at', 'updated_at',)

class CommentSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    community = CommunitySerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('user', 'community', 'content', 'created_at', 'id')
        