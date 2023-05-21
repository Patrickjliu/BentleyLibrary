# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bookinventory(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13)
    published_date = models.DateField()
    publisher = models.CharField(max_length=255)
    quantity = models.IntegerField()
    available_quantity = models.IntegerField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bookinventory'


class Log(models.Model):
    book = models.ForeignKey(Bookinventory, models.DO_NOTHING)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13)
    borrower_first_name = models.CharField(max_length=255)
    borrower_last_name = models.CharField(max_length=255)
    borrower_email = models.CharField(max_length=255)
    borrowed_date = models.DateField()
    borrowed_time = models.TimeField()
    returned_date = models.DateField(blank=True, null=True)
    returned_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log'
