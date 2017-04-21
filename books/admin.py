# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Book, Author, BookComment

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookComment)
# Register your models here.
