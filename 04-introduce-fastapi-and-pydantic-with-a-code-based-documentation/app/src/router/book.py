from typing import Sequence

from fastapi import APIRouter, status

from src.schema import Book


router = APIRouter()


@router.get(
    path="/books",
    response_model=Sequence[Book],
    status_code=status.HTTP_200_OK
)
async def get_books():
    """
    Description \n
        1. Get all books.

    To-do \n
        1. Search by name with query parameter.
    """
    return [
        Book(name="Demian"),
        Book(name="Siddhartha")
    ]
