from django.shortcuts import render
from shelf.models import *

# Create your views here

def index(request):

    return render(request, 'index.html')


def books(request):


    return render(request, 'booklist.html')

def book(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'book.html', {'book': book})
