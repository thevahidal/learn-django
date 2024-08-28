from django.urls import path

from books.views import get_one_book, list_all_books


urlpatterns = [
    path("all-books/", list_all_books),
    path("all-books/<book_id>/", get_one_book),
]
