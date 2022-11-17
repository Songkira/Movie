from django.contrib.auth import get_user_model
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
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

# @api_view(['POST'])
# def follow_count(request, person_pk):
#     person = get_object_or_404(get_user_model(), pk=person_pk)
#     followings = person.followings.filter()
#     followers = person.followers.filter()
#     print(11111)
#     print(person)
#     print(followings, followers)