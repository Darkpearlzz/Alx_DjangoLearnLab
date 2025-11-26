from django.db import models

class Author(models.Model):
    """
    Author model:
    - name: stores the author's full name as text.
    - The Author has a one-to-many relationship with Book (one Author -> many Books).
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model:
    - title: title of the book.
    - publication_year: integer year when the book was published.
    - author: ForeignKey to Author — establishes the one-to-many (Author -> Books).
      We use on_delete=models.CASCADE so if an author is deleted, their books are removed too.
    """
    title = models.CharField(max_length=512)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
