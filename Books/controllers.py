from ninja_extra import api_controller, route
from . import models
from django.shortcuts import get_object_or_404
from . import schema
from typing import List


@api_controller("/")
class BookController:

    @route.get("/books", response=List[schema.BookSchema])
    def list_books(self, request):
        books = models.Book.objects.all()
        return [schema.BookSchema.from_orm(book) for book in books]

    @route.post("/books", response=schema.BookSchema, auth=None)
    def create_book(self, request, payload: schema.BookSchema):
        book = models.Book.objects.create(
            title=payload.title,
            author=payload.author
        )
        return schema.BookSchema.from_orm(book)

    @route.get("/books/{book_id}", response=schema.BookSchema)
    def get_book(self, request, book_id: int):
        book = get_object_or_404(models.Book, id=book_id)
        return schema.BookSchema.from_orm(book)