from .models import *

def allBooks(request):


        comicBooks = Book.objects.filter(comic_books=True).order_by('-pub_date')
        actionBooks = Book.objects.filter(action_books=True).order_by('-pub_date')
        fantasyBooks = Book.objects.filter(fantasy_books=True).order_by('-pub_date')
        contemporaryBooks = Book.objects.filter(contemporary_books=True).order_by('-pub_date')
        thrillerBooks = Book.objects.filter(thriller_books=True).order_by('-pub_date')


        context = {
           'comicBooks':comicBooks,
           'actionBooks':actionBooks,
           'fantasyBooks':fantasyBooks,
           'contemporaryBooks':contemporaryBooks,
           'thrillerBooks':thrillerBooks
        }

        return context