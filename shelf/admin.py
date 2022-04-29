from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Customer)
admin.site.register(Book)
admin.site.register(Bookshelf)
admin.site.register(Category)
admin.site.register(Shelved)
admin.site.register(Archive)
admin.site.register(Archived)

