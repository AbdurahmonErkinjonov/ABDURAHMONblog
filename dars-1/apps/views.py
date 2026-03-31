from django.shortcuts import render
from fastapi import Response
from .models import Author, Genre, Book
from .serializers import AuthorSerializer, GenreSerializer, BookSerializer   
from rest_framework.views import APIView
from rest_framework.response import Response


class AuthorAPIView(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(AuthorSerializer(Author).data, status=201)
        return Response(serializer.errors, status=400)
    
    
class GenreAPIView(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(GenreSerializer(Genre).data, status=201)
        return Response(serializer.errors, status=400)      
    
class BookAPIView(APIView):     
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(BookSerializer(Book).data, status=201)
        return Response(serializer.errors, status=400)      
    