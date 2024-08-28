from django.http.response import JsonResponse
from books.models import Book

from rest_framework.response import Response
from rest_framework.decorators import api_view

from books.serializers import BooksSerializer


@api_view()
def list_all_books(request):
    books = Book.objects.all()

    return Response(BooksSerializer(books, many=True).data)


@api_view()
def get_one_book(request, **kwargs):
    book = Book.objects.filter(id=kwargs.get("book_id")).first()

    if not book:
        return Response({"message": "Book not found"}, status=404)

    return Response(BooksSerializer(book).data)
