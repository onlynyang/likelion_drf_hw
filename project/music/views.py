from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Singer, Song, Comment
from .serializers import SingerSerializer, SongSerializer, CommentSerializer

from django.shortcuts import get_object_or_404
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def song_list_create(request):

    if request.method == 'GET':
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(data=serializer.data)
    
    if request.method == 'POST':
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data)

@api_view(['GET', 'POST'])
def singer_list_create(request):

    if request.method == 'GET':
        singers = Singer.objects.all()
        serializer = SingerSerializer(singers, many=True)
        return Response(data=serializer.data)
    
    if request.method == 'POST':
        serializer = SingerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data)

@api_view(['GET', 'PATCH', 'DELETE'])
def singer_detail_update_delete(request, singer_id):
    singer = get_object_or_404(Singer, id=singer_id)

    if request.method == 'GET':
        serializer = SingerSerializer(singer)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        serializer = SingerSerializer(instance=singer, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        singer.delete()
        data = {
            'deleted_singer': singer_id
        }
        return Response(data)

@api_view(['GET', 'PATCH', 'DELETE'])
def song_detail_update_delete(request, song_id):
    song = get_object_or_404(Song, id=song_id)

    if request.method == 'GET':
        serializer = SongSerializer(song)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        serializer = SongSerializer(instance=song, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        song.delete()
        data = {
            'deleted_song': song_id
        }
        return Response(data)

@api_view(['GET', 'POST'])
def comment_read_create(request, song_id):
    song = get_object_or_404(Song, id=song_id)

    if request.method == 'GET':
        comments = Comment.objects.filter(song=song)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        data = {
            'song': song_id,
            'singer': song.singer.id,
            'writer': request.data.get('writer', 'Unknown'),
            'content': request.data.get('content', '')
        }
        
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors) 
