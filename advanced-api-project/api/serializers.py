from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    BookSerializer:
    - Serializes all fields of Book: id, title, publication_year, author.
    - Adds custom validation to ensure publication_year is not in the future.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """
        Field-level validation for publication_year.
        Ensure year is not in the future.
        """
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("publication_year cannot be in the future.")
        return value


class BookNestedSerializer(serializers.ModelSerializer):
    """
    A lightweight serializer used for nested representation of books inside AuthorSerializer.
    We include id, title, and publication_year. 'author' is omitted to avoid cycles.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year']


class AuthorSerializer(serializers.ModelSerializer):
    """
    AuthorSerializer:
    - Serializes the Author name and a nested list of the author's books.
    - books: dynamically loads related Book objects using the related_name 'books' declared in models.
    - The nested BookNestedSerializer is read-only by default, meaning Author creation/update won't create Book objects.
      (See the WritableNestedAuthorSerializer example below if you need nested create/update.)
    """
    books = BookNestedSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

class WritableBookNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year']

class WritableNestedAuthorSerializer(serializers.ModelSerializer):
    books = WritableBookNestedSerializer(many=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

    def create(self, validated_data):
        books_data = validated_data.pop('books', [])
        author = Author.objects.create(**validated_data)
        for book_data in books_data:
            Book.objects.create(author=author, **book_data)
        return author

    def update(self, instance, validated_data):
        # Simple strategy: replace all books. More sophisticated merging logic can be added.
        books_data = validated_data.pop('books', [])
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        # remove existing books and recreate
        instance.books.all().delete()
        for book_data in books_data:
            Book.objects.create(author=instance, **book_data)
        return instance
