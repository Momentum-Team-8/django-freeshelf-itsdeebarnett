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

    def __str__(self):
        return self.title
