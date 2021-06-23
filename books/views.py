from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Book

# Create your views here.
def homepage(request):
    if request.user.is_authenticated:
        return redirect ("book_list")
    return render(request, "books/homepage.html")


@login_required # this is a decorator or function that will redirect you to login page
def book_list(request):
    books = Book.objects.all().order_by("title")
    return render(request, "books/books_list.html", {"books": books})
