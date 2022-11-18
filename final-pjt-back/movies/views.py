from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieSerializer, GenreSerializer, ActorSerializer, DirectorSerializer, CommentSerializer, StarSerializer
from .models import Movie, Actor, Director, Genre, Comment, Star


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
    genres = movie.genres.values()
    director = movie.director.values()
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        data = serializer.data
        data['director'] = director[0]
        data['genres'] = genres
        return Response(data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = CommentSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, movie=movie)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def star_test(request, movie_pk):
    if request.method == 'GET':
        print(0)
        stars = Star.objects.all().filter(movie_id=movie_pk)
        serializer = StarSerializer(stars, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serialzer = StarSerializer(data=request.data)

        if serialzer.is_valid(raise_exception=True):
            print(request.data)
            movie = get_object_or_404(Movie, pk=movie_pk)
            pre_point = movie.vote_average * movie.vote_count
            pre_count = movie.vote_count

            point = pre_point + request.data.get('rank')
            count = movie.vote_count + 1
            new_vote_average = round(point/count, 1)

            movie.vote_average = new_vote_average
            movie.vote_count = count
            
            movie.save()
            serialzer.save(user=request.user)
            return Response(movie.vote_average)

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
@permission_classes([IsAuthenticated])
def comment_list(request, movie_pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        comments = movie.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def comment_delete(request, movie_pk, comment_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    comment = movie.comment_set.get(pk=comment_pk)
    if not request.user.comments.filter(pk=comment_pk).exits():
        return Response({'message': '권한이 없습니다.'})
    else:
        comment.delete()
        result = { '댓글 삭제'}
        return Response(result)
    

@api_view(['GET', 'POST'])
def likes(request, movie_pk, user_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = get_object_or_404(get_user_model(), pk=user_pk)
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

@api_view(['GET'])
def likemovies(request, person_pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=person_pk)
    movies = user.like_movies.values()
    return Response(movies, status=status.HTTP_200_OK)

@api_view(['GET'])
def mycomments(request, person_pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=person_pk)
    comments = user.comment_set.values()
    return Response(comments, status=status.HTTP_200_OK)

