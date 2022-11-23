from rest_framework import serializers
from .models import Genre, Actor, Director, Movie, Comment, Star, Review

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'

class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    catpic = serializers.SerializerMethodField()

    def get_username(self, obj):
        return obj.user.username

    def get_catpic(self, obj):
        return obj.user.catpic
    
    class Meta:
        model = Comment
        fields = ( 'id','content','user','username', 'movie', 'catpic')
        # fields = ('content',)
        read_only_fields = ( 'user', 'movie')

class StarSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    def get_username(self, obj):
        return obj.user.username

    class Meta:
        model = Star
        fields = ( 'id','user','username', 'movie', 'rank', )
        # fields = ('content',)
        read_only_fields = ( 'user', )

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'