from django import forms
from .models import Book
import re

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'description', 'isbn']

    def clean_title(self):
        title = self.cleaned_data.get('title', '').strip()

        if len(title) < 2:
            raise forms.ValidationError("Title must be at least 2 characters long.")

        if len(title) > 200:
            raise forms.ValidationError("Title is too long.")

        return title

    def clean_description(self):
        description = self.cleaned_data.get('description', '').strip()

        if not description:
            raise forms.ValidationError("Description cannot be empty.")

        # Basic XSS guard — Django escapes output automatically
        # but we still disallow script tags
        if "<script>" in description.lower():
            raise forms.ValidationError("Invalid content detected in description.")

        return description

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn', '').strip()

        # Must be exactly 13 digits
        if not re.fullmatch(r"\d{13}", isbn):
            raise forms.ValidationError("ISBN must be exactly 13 digits.")

        return isbn
