from django.urls import path
from .views import AuthorAPIView, GenreAPIView, BookAPIView
urlpatterns = [
    path('authors/', AuthorAPIView.as_view(), name='author-list'),  
    path('genres/', GenreAPIView.as_view(), name='genre-list'),
    path('books/', BookAPIView.as_view(), name='book-list'),
]