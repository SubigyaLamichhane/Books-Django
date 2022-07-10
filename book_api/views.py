from django.shortcuts import render
from book_api.models import Book
from django.http import JsonResponse

# Create your views here.
def book_list(request):
    books = Book.objects.all() # get all books from the database Complex Data
    booksPython = list(books.values()) # convert to list Python object
    return JsonResponse({
      'books': booksPython
    })