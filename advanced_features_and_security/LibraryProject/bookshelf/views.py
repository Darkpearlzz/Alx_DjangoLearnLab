from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from .models import Book
from .forms import BookForm

# -------------------------------
# SECURE BOOK LIST VIEW
# -------------------------------
@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """
    Shows list of books.
    Enhanced to support safe search input.
    """
    books = Book.objects.all()

    # Optional: Secure search feature
    query = request.GET.get("search", "").strip()
    if query:
        # ORM filtering — safe against SQL Injection
        books = books.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )

    return render(request, 'bookshelf/list_books.html', {
        'books': books,
        'query': query
    })


# -------------------------------
# SECURE BOOK CREATE VIEW
# -------------------------------
@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    """
    Secure book creation using Django forms to validate input.
    Automatically protected by CSRF middleware.
    """
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():  # validates input, prevents XSS & injection
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()

    return render(request, 'bookshelf/book_form.html', {
        'form': form
    })


# -------------------------------
# SECURE BOOK EDIT VIEW
# -------------------------------
@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    """
    Allows editing a book safely.
    Uses form validation and ORM to avoid manual SQL.
    """
    book = get_object_or_404(Book, pk=pk)

    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')

    return render(request, 'bookshelf/book_form.html', {
        'form': form
    })


# -------------------------------
# SECURE BOOK DELETE VIEW
# -------------------------------
@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    """
    Secure delete view — deletes only on POST request.
    Prevents CSRF + ensures proper permission checks.
    """
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':  # prevents accidental deletes
        book.delete()
        return redirect('book_list')

    return render(request, 'bookshelf/confirm_delete.html', {
        'object': book
    })
