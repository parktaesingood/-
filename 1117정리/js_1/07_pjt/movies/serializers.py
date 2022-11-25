from rest_framework import serializers
from .models import Movie, Actor, Review


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title','overview',)


class MovieSerializer(serializers.ModelSerializer):
    class ActorListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('name',)
    actors = ActorListSerializer(many=True,read_only =True) 

    class ReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('title','content')
    review = ReviewSerializer(many=True,read_only =True)
    
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('title',)

class MovietitleSerializer(serializers.ModelSerializer):
   class Meta:
        model = Movie
        fields = ('title',)
 
class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):
    movies = MovietitleSerializer(many=True,read_only =True)
    class Meta:
        model = Actor
        fields = '__all__'


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title','content',)
        


class ReviewSerializer(serializers.ModelSerializer):
    movie = MovietitleSerializer(read_only =True)
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie',)
                


