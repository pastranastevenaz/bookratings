# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Book(models.Model):
    author = models.ForeignKey('Author')
    title = models.CharField(max_length=100)
    isbn = models.CharField(unique=True, max_length=13)
    summary = models.TextField()

    def __str__(self):
        return self.title

class BookComment(models.Model):
    commentor = models.CharField(max_length=30, blank=False, null=True)
    comment = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True, null=True)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.comment

class Author(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)

    def __str__(self):
        return self.last_name + ", " + self.first_name
