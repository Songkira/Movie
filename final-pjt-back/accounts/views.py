from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        account = serializer.save()
        token = Token.objects.create(user=account).key
        data = {
            'username': account.username,
            'password': account.password,
            'token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#6b104660bdcbe43b6703812ea9ac605aaf7e797d