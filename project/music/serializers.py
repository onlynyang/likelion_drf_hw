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

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']

class SingerSerializer(serializers.ModelSerializer):

    tag = serializers.SerializerMethodField()
    images = ImageSerializer(many=True, read_only=True)

    def get_tag(selg, instance):
        tags = instance.tag.all()
        return [tag.name for tag in tags]

    class Meta:
        model = Singer
        fields = '__all__'

    image = serializers.ImageField(use_url=True, required=False)

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fidels = '__all__'

