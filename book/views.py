from django.shortcuts import render, redirect
from django.db.models import Sum, Max, Min, Avg, Count, Q

from .models import Book


def book(request):
    book = Book.objects.using("book_db").all()
    data = Book.objects.aggregate(sum=Sum('ratings_count'), max=Max(
        'ratings_count'), min=Min('ratings_count'), avg=Avg('ratings_count'))

    rating_diff = Book.objects.aggregate(rating_diff=Max(
        'ratings_count') - Avg('ratings_count'))

    oldest_pub_date = Book.objects.aggregate(oldest_pub_date=Min('publication_date'))
    tr_price = Book.objects.filter(title__startswith="Treasure").aggregate(Avg("ratings_count"))


    context = {
        'book': book,
        'data': data,
        'rating_diff': rating_diff,
        'oldest_pub_date': oldest_pub_date,
        'tr_price': tr_price
    }

    return render(request, "book/book.html", context)
