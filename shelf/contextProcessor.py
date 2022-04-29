from .models import *

def allBooks(request):


        comicBooks = Book.objects.filter(comic_books=True).order_by('-id')    
        actionBooks = Book.objects.filter(action_books=True).order_by('-id')
        fantasyBooks = Book.objects.filter(fantasy_books=True).order_by('-id')
        contemporaryBooks = Book.objects.filter(contemporary_books=True).order_by('-id')
        ThrillerBooks = Book.objects.filter(thriller_books=True).order_by('-id')

        print(actionBooks)
        print(comicBooks)

        context = {
           'comicBooks':comicBooks,
           'actionBooks':actionBooks,
           'fantasyBooks':fantasyBooks,
           'contemporaryBooks':contemporaryBooks,
           'ThrillerBooks':ThrillerBooks
        }
       
        return context