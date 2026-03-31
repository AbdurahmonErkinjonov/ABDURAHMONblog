from .models import Author, Genre, Book
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class AuthorSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=100)
    birth_date = serializers.DateField()
    
    def create(self, validated_data):
        return Author.objects.create(**validated_data)
    


class GenreSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    
    def create(self, validated_data):
        return Genre.objects.create(**validated_data)   
    
    
    
class BookSerializer(serializers.Serializer):       
    title = serializers.CharField(max_length=200)
    author = AuthorSerializer()
    published_date = serializers.DateField()
    page = serializers.IntegerField()
    price = serializers.IntegerField()
    image = serializers.URLField()
    genre = GenreSerializer(many=True)
    description = serializers.CharField()
    
    def create(self, validated_data):
        author_data = validated_data.pop('author')
        genre_data = validated_data.pop('genre')
        
        author, created = Author.objects.get_or_create(**author_data)
        book = Book.objects.create(author=author, **validated_data)
        
        for genre in genre_data:
            genre_obj, created = Genre.objects.get_or_create(**genre)
            book.genre.add(genre_obj)
        
        return book
    
