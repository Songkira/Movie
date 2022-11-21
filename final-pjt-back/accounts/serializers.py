from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'password', 'sex', 'birth', 'nofear', 'nothrill')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User(
            username = validated_data['username'],
            sex = validated_data['sex'],
            birth = validated_data['birth'],
            nofear = validated_data['nofear'],
            nothrill = validated_data['nothrill'],
            )
        user.set_password(validated_data['password'])
        user.save()
        return user