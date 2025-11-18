from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'isbn']


# Used for demonstrating CSRF, XSS protection, and secure user input handling
class ExampleForm(forms.Form):
    user_input = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Type something...'})
    )
