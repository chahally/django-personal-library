# Create your models here.

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    read = models.BooleanField(default=False)
    
    def __str__(self):
        # String representation of the book
        # Useful for admin interface and shell
        return f"{self.title} by {self.author}"