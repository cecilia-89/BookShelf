from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, SET_NULL

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    userName = models.CharField(max_length=50, null=True,blank=True)

    def __str__(self):
        return self.user.userName

class Category(models.Model):
    type = models.CharField(max_length=50, null=True,blank=True)

    def __str__(self):
        return self.type

class Book(models.Model):
    title = models.CharField(max_length=50, null=True,blank=True)
    author = models.CharField(max_length=50, null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True, blank=True)
    pub_date = models.DateField()
    image = models.ImageField(blank=False)
    description = models.TextField()
    comic_books = models.BooleanField(default=False)
    action_books = models.BooleanField(default=False)
    contemporary_books = models.BooleanField(default=False)
    thriller_books = models.BooleanField(default=False)
    fantasy_books = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @property
    def bookUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Bookshelf(models.Model):
    customer = models.ForeignKey(Customer, on_delete=CASCADE)
    book = models.ForeignKey(Book, on_delete=SET_NULL, null=True)


