from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    book_url = models.URLField()
    description = models.TextField()
    created_by = models.DateTimeField(default=timezone.now)
    Categories = models.ManyToManyField("Category", related_name="books")

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=75)

    def repr(self):
        return f"<Category name={self.name}>"

    def str(self):
        return self.name