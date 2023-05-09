from django.contrib import admin

from book.models import Book, Store, Publisher, Author

admin.site.register(Book)
admin.site.register(Store)
admin.site.register(Publisher)
admin.site.register(Author)