from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13)
    published_date = models.DateField()
    publisher = models.CharField(max_length=255)
    quantity = models.IntegerField()
    available_quantity = models.IntegerField()
    description = models.TextField(blank=True)

class Log(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13)
    borrower_first_name = models.CharField(max_length=255)
    borrower_last_name = models.CharField(max_length=255)
    borrower_email = models.EmailField()
    borrowed_date = models.DateField()
    borrowed_time = models.TimeField()
    returned_date = models.DateField(null=True, blank=True)
    returned_time = models.TimeField(null=True, blank=True)
