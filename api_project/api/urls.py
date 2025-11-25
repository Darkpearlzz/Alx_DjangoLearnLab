from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

    # Create the router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Keep the list-view endpoint
    path('books/', BookList.as_view(), name='book-list'),

    # Include all ViewSet CRUD routes
    path('', include(router.urls)),
]
