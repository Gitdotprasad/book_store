from django.shortcuts import render,get_object_or_404
from .models import book
from django.http import Http404
from django.db.models import Avg
# Create your views here.


def index(request):
    books = book.objects.all().order_by("rating")
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))


    return render(request, "book_outlet/index.html", {
        "books": books,
        "total_number_of_books": num_books,
        "average_rating": avg_rating
        })


def book_detail(request,slug):
    # try:
    #     books = book.objects.get(pk=id)
    # except:
    #     raise Http404()

    books = get_object_or_404(book, slug=slug)
      
    return render(request, "book_outlet/book_detail.html",{
        "title": books.title,
        "author": books.author,
        "rating": books.rating, 
        "is_bestdeller": books.is_bestselling
    })
     