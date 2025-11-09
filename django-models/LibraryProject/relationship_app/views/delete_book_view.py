from django.shortcuts import render
from django.contrib.auth.decorators import permission_required

@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id):
    # Your logic to delete a book
    pass
