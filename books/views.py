# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render


from .models import Book, BookComment

def index(request):
    book_list = Book.objects.order_by('title')[:10]
    context = {'book_list':  book_list}
    return render(request, 'books/index.html', context)

    # HOW TO RENDR THE TEMPLATE VIEW USING HTTP RESPONSE INSTEAD OF THE RENDR SHORTCUT
    # template = loader.get_template('books/index.html')
    # context = {
    #     'book_list': book_list,
    # }
    # return HttpResponse(template.render(context, request))

    # output = ', '.join([b.title for b in book_list])
    # return HttpResponse(output)
    # return HttpResponse("Hello from the books index view")

def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book_comm = get_object_or_404(BookComment, pk=book_comment_id)
    return render(request, 'books/detail.html', {'book': book, 'book_comm': book_comm})
    
    # try:
    #     book = Book.objects.get(pk = book_id)
    # except Book.DoesNotExist:
    #     raise Http404("This book does not exist!")
    # return render(request, 'books/detail.html', {'book': book})

    # return HttpResponse("You are looking at book %s." % book_id)
