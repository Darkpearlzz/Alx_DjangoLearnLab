from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]     # Requires token login


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Example: Only authenticated users can access CRUD
    permission_classes = [IsAuthenticated]

    # Optional: restrict delete/update to admin only
    # permission_classes = [IsAdminUser]
