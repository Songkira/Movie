from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieSerializer, GenreSerializer, ActorSerializer, DirectorSerializer, CommentSerializer
from .models import Movie, Actor, Director, Genre, Comment


# Create your views here.
@api_view(['GET'])
def movies_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = CommentSerializer(data=request.data)
    print(3, request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user, username=request.username)
        return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data, partial = True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        comment.delete()
        result = { '댓글 삭제'}
        return Response(result)

@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def likes(request, movie_pk, user_pk):
    print(0)
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = get_object_or_404(get_user_model(), pk=user_pk)
    print(1)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    elif request.method == 'POST':
        if movie.like_users.filter(pk=user_pk).exists():
            movie.like_users.remove(user)
            # following = False
        else:
            movie.like_users.add(user)
            # following = True
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)
            # return Response(serializer.data)