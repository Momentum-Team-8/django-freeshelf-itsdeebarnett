from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Book, Category

# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return redirect ("list_books")
    return render(request, "books/homepage.html")


@login_required # this is a decorator or function that will redirect you to login page
def book_list(request):
    books = Book.objects.all().order_by("title")
    return render(request, "books/books_list.html", {"books": books})

def categories_books(request, slug):
    category = get_object_or_404(Category, slug=slug)
    books = category.books.all()

    return render(request, "books/categories_books.html", {"category": category, "books": books})