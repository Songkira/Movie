from django.contrib.auth import get_user_model
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSerializer


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow(request, my_pk, person_pk):
    me = get_object_or_404(get_user_model(), pk=my_pk)
    person = get_object_or_404(get_user_model(), pk=person_pk)
    if person != me:
        if person.followers.filter(pk=my_pk).exists():
            person.followers.remove(me)
            following = False
        else:
            person.followers.add(me)
            following = True
        return Response(following, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

#6b104660bdcbe43b6703812ea9ac605aaf7e797d

@api_view(['GET'])
def usersinfo(request):
    User = get_user_model()
    users = User.objects.values()
    return Response(users, status=status.HTTP_200_OK)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT',])
@permission_classes([IsAuthenticated])
def myinfo(request, my_pk):
    User = get_user_model()
    if request.method == 'GET':
        user = User.objects.values().filter(pk=my_pk)
        return Response(user, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        user = get_object_or_404(User, pk=my_pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def followinfo(request, person_pk):
    person = get_object_or_404(get_user_model(), pk=person_pk)
    followings = person.followings.values()
    followers = person.followers.values()
    data = { 'followers':followers, 'followings':followings }
    return Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
def userlikelist(request, person_pk):
    person = get_object_or_404(get_user_model(), pk=person_pk)
    likemovies = person.like_movies.values()
    return Response(likemovies, status=status.HTTP_200_OK)