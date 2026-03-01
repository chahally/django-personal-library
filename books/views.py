# Create your views here.

from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

def home(request):
    """
    Home page view.
    Fetches all Book objects and passes them to the template.
    """
    books = Book.objects.all()
    return render(request, 'books/home.html', {'books': books})

def add_book(request):
    """
    View to add a new book to the library.
    Handles both GET (show form) and POST (submit form) requests.
    """
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            # Save the new book to the database
            form.save()
            # Redirect to home page after successful save
            return redirect('home')
    else:
        # If GET request, create empty form
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})