from django.shortcuts import render
from shelf.models import Archive, Archived, Book, Bookshelf, Shelved
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import *
from django.http.response import JsonResponse
import json
from django.contrib.auth import authenticate, login, logout

# Create your views here

def index(request):

    return render(request, 'index.html')


def books(request):

    return render(request, 'booklist.html')

def book(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'book.html', {'book': book})

def auth(request):
    form = registerForm
    if request.method == 'POST':
        if request.POST.get('submit') == 'login':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')

            messages.success(request, ('An error   occured. Please fill in your details   correctly.'))
            return redirect('/auth')

        if request.POST.get('submit') == 'signup':
            form = registerForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data ['username']
                password = form.cleaned_data ['password1']
                authenticate(request,  username=username,     password=password)
                return redirect('/auth')

            form = registerForm()



    return render(request, 'login.html', {'form':form})


def signout(request):
    logout(request)
    return redirect('/auth')


def addRead(request):

    data = json.loads(request.body)
    bookId = data['bookId']
    action = data['action']

    customer = request.user.customer
    shelf = Bookshelf.objects.get(customer=customer)
    book = Book.objects.get(id=bookId)
    shelf, created = Bookshelf.objects.get_or_create(book=book, shelf=shelf)

    if action =='move':
        archived = Archived.objects.get(book=book)
        archived.delete()

    shelf.save()

    if action == 'delete':
        shelf.delete()


def archived(request):
    data = json.loads(request.body)
    bookId = data['bookId']
    action = data['action']

    customer = request.user.customer
    archive = Archive.objects.get(customer=customer)
    book = Shelved.objects.get(id=bookId)
    archived, created = Archive.objects.get_or_create(book=book, archive=archive)

    archived.save()

    if action == 'delete':
        archived.delete()