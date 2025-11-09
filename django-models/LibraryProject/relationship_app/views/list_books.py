from django.shortcuts import render
from ..models import Book  # or 'from relationship_app.models import Book'

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})
