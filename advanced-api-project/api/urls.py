from django.urls import path
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import AuthorViewSet, BookViewSet
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    path("books/", BookListView.as_view(), name="book-list"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("books/create/", BookCreateView.as_view(), name="book-create"),
    path("books/update/", BookUpdateView.as_view(), name="book-update-no-id"),
    path("books/delete/", BookDeleteView.as_view(), name="book-delete-no-id"),
]

router = routers.DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

urlpatterns = router.urls
