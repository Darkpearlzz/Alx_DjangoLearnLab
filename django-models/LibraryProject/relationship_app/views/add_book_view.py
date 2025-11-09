from django.shortcuts import render
from django.contrib.auth.decorators import permission_required

@permission_required('relationship_app.can_add_book')
def add_book(request):
    # Your logic to add a book
    pass
