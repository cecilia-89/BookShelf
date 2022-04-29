from django.shortcuts import render
from shelf.models import *

# Create your views here

def index(request):

    return render(request, 'index.html', {'books':books})


def books(request):
    
    return render(request, 'booklist.html',{'lists':lists})

def book(request, book_id):
    
    return render(request, 'book.html',{'book':book})
