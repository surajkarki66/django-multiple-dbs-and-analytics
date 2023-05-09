from django.shortcuts import render, redirect
from django.db.models import Avg, Max, Min, FloatField, Count, Q, Sum

from .models import Book, Publisher, Author, Store


def book(request):
    book = Book.objects.using("book_db").all()
    # Aggregations

    # Total number of books.
    total_books_count = Book.objects.count()

    # Total number of books with publisher=Bloomsbury
    total_no_of_bloomsbury_books = Book.objects.filter(
        publisher__name="Bloomsbury").count()

    # Average price across all books.
    avg_price = Book.objects.aggregate(Avg('price'))

    # Max price across all books.
    max_price = Book.objects.aggregate(Max('price'))

    # Max price across all books.
    min_price = Book.objects.aggregate(Min('price'))

    # Difference between the highest priced book and the average price of all books.
    price_diff = Book.objects.aggregate(price_diff=Max("price") - Avg("price"))

    #We can also ask for the oldest book of any of those managed by every publisher:
    oldest_book_pubdate = Publisher.objects.aggregate(oldest_pubdate=Min('book__pubdate'))
    print(oldest_book_pubdate)

    #you can generate the average price of all books with a title that starts with “Harry” using the query:
    avg_price = Book.objects.filter(name__startswith="Harry").aggregate(Avg('price'))
    print(avg_price)

    
    
    
    
    # Annotations

    # Each publisher, each with a count of books as a "num_books" attribute.
    pub_with_books = Publisher.objects.annotate(num_books=Count('book'))
    print(vars(pub_with_books[0]))

    # Each publisher, with a separate count of books with a rating above and below 5
    above_5 = Count("book", filter=Q(book__rating__gt=5))
    below_5 = Count("book", filter=Q(book__rating__lte=5))

    x = Publisher.objects.annotate(below_5=below_5).annotate(above_5=above_5)
    print(vars(x[0]))

    # The top 5 publishers, in order by number of books.
    top_5_pub = Publisher.objects.annotate(
        num_books=Count('book')).order_by("-num_books")[:5]
    print(top_5_pub)
    print(top_5_pub[0].num_books)

    # show no of authors of each book
    no_of_author = Book.objects.annotate(Count('authors'))
    print(vars(no_of_author[0])['authors__count'])
    print(vars(no_of_author[1])['authors__count'])
    print(vars(no_of_author[2])['authors__count'])
    print(vars(no_of_author[3])['authors__count'])

    # show no of books written by each author
    no_of = Author.objects.annotate(
        num_books=Count('book')).order_by("-num_books")[:5]
    print(vars(no_of[0])['num_books'])
    print(vars(no_of[1])['num_books'])
    print(vars(no_of[2])['num_books'])
    print(vars(no_of[3])['num_books'])

    # combining multiple aggregations
    qs = Book.objects.annotate(
        Count('authors', distinct=True), Count('store', distinct=True))
    print(vars(qs[0]))
    print('---------------------')
    # to find the price range of books offered in each store, you could use the annotation:
    price_range = Store.objects.annotate(min_price=Min(
        'books__price'), max_price=Max('books__price'))

    print(vars(price_range[0])['min_price'])
    print(vars(price_range[0])['max_price'])
    print('---------------------')
    print(vars(price_range[1])['min_price'])
    print(vars(price_range[1])['max_price'])
    print('---------------------')
    print(vars(price_range[2])['min_price'])
    print(vars(price_range[2])['max_price'])

    print('---------------------')
    print(vars(price_range[3])['min_price'])
    print(vars(price_range[3])['max_price'])
    print('---------------------')

    # we can ask for all publishers, annotated with their respective total book stock counters:
    pubs = Publisher.objects.annotate(total_book_stock=Count('book', distinct=True))
    print(vars(pubs[0]))
    print(vars(pubs[1]))

    print('---------------------')


    #we can ask for every author, annotated with the total number of pages considering all the books the author has (co-)authored 
    author = Author.objects.annotate(total_no_of_pages=Sum('book__pages'))
    print(vars(author[0]))

    print('---------------------')

    #ask for the average rating of all the books written by author(s) we have on file:
    avg_rate = Author.objects.annotate(avg_rating=Avg('book__rating'))
    print(vars(avg_rate[0]))
    print(vars(avg_rate[1]))
    print(vars(avg_rate[2]))
    print(vars(avg_rate[3]))

    print('---------------------')

    #you can generate an annotated list of all books that have a title starting with Harry using the query:
    book_s = Book.objects.filter(name__startswith="Harry").annotate(no_stores=Count('store'))
    print(vars(book_s[0]))
    print(vars(book_s[1]))

    print('---------------------')

    #Filtering on annotations
    #to generate a list of books that have more than one author, you can issue the query:
    li_books = Book.objects.annotate(no_of_author=Count('authors')).filter(no_of_author__gt=1)
    print(vars(li_books[0]))
    print(vars(li_books[1]))
    print(vars(li_books[2]))

    print('---------------------')
    
    #If you need two annotations with two separate filters you can use the filter argument with any aggregate.
    #For example, to generate a list of authors with a count of highly rated books:
    highly_rated = Count("book", filter=Q(book__rating__gte=7))
    li_authors = Author.objects.annotate(num_books=Count('book'), no_of_highly_rated_books=highly_rated)
    print(vars(li_authors[0]))

    print('---------------------')

    # to order a QuerySet of books by the number of authors that have contributed to the book, you could use the following query:
    qs4 = Book.objects.annotate(num_authors=Count('authors', distinct=True)).order_by("-num_authors") # descending order
    print(vars(qs4[0]))

    print('---------------------')
    #consider an author query that attempts to find out the average rating of books written by each author:
    authors_r = Author.objects.annotate(avg_rating=Avg('book__rating'))
    print(vars(authors_r[0]))
    print(vars(authors_r[1]))

    print('---------------------')

    authors_s = Author.objects.values('name').annotate(avg_rating=Avg('book__rating'))
    print(authors_s)
    print(vars(authors_s))

    #print(Author.objects.values('name').order_by('age'))

    #  if you wanted to calculate the average number of authors per book
    avg_auth = Book.objects.annotate(num_authors=Count('authors', distinct=True)).aggregate(Avg('num_authors'))
    print(avg_auth)



    context = {
        'book': book,
        'total_books_count': total_books_count,
        'total_no_of_bloomsbury_books': total_no_of_bloomsbury_books,
        'avg_price': avg_price,
        'max_price': max_price,
        'min_price': min_price,
        'price_diff': price_diff
    }
    return render(request, "book/book.html", context)
