from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    """
    Form for creating or updating Book instances.
    Uses all fields from the Book model.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'read']