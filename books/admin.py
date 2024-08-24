from django.contrib import admin

from books.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "pages", "isbn"]
    list_filter = ["is_active"]
    search_fields = ["title", "isbn"]
