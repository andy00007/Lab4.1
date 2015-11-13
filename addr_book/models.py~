# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models


class Author(models.Model):
    authorid = models.CharField(max_length=60, primary_key=True, db_column='AuthorID') # Field name made lowercase.
    name = models.CharField(max_length=90, db_column='Name') # Field name made lowercase.
    age = models.CharField(max_length=30, db_column='Age', blank=True) # Field name made lowercase.
    country = models.CharField(max_length=90, db_column='Country', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'author'

class Book(models.Model):
    isbn = models.CharField(max_length=30, primary_key=True, db_column='ISBN') # Field name made lowercase.
    title = models.CharField(max_length=150, db_column='Title') # Field name made lowercase.
    publisher = models.CharField(max_length=150, db_column='Publisher', blank=True) # Field name made lowercase.
    publishdate = models.CharField(max_length=90, blank=True) # Field name made lowercase.
    price = models.CharField(max_length=60, db_column='Price', blank=True) # Field name made lowercase.
    authorid = models.ForeignKey(Author, null=True, db_column='AuthorID', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'book'


