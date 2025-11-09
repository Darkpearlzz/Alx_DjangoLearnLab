from django.shortcuts import render
from django.contrib.auth.decorators import permission_required

@permission_required('relationship_app.can_change_book')
def edit_book(request, book_id):
    # Your logic to edit a book
    pass
