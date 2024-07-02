from rest_framework import serializers
from .models import *

class SongSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    comments = serializers.SerializerMethodField(read_only=True)

    def get_comments(self, instance):
        serializer = CommentSerializer(instance.comments, many=True)
        return serializer.data

    class Meta:
        model = Song
        fields = ['id', 'title', 'singer', 'release', 'content', 'comments']

class SingerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Singer
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
