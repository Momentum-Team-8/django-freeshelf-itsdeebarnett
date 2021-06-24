from books.models import Book, Category, User
from django.contrib import admin

# Register your models here.
admin.site.register(Book)
admin.site.register(User)
admin.site.register(Category)
