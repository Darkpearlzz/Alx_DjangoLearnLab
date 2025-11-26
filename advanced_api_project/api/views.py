from rest_framework import viewsets
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    """
    CRUD endpoints for Author.
    The AuthorSerializer includes nested books (read-only).
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    CRUD endpoints for Book.
    BookSerializer enforces publication_year validation.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
