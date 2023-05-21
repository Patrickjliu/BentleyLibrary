from django.db import models

class BookInventory(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13)
    published_date = models.DateField()
    publisher = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    available_quantity = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title

from core.models import BookInventory