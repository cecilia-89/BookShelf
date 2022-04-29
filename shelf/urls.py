from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name = 'index'),
    path('books/', views.books, name = 'list'),
    path('book/<int:book_id>', views.book, name = 'product'),
    path('signout/', views.signout, name = 'signout'),
    path('auth/', views.auth, name = 'auth'),
]
