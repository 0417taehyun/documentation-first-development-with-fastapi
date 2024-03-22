from typing import Annotated

from fastapi import APIRouter, status, Query

from src.constant import Country, Language
from src.schema import (
    v2,
    NotFoundErrorResponse,
    InternalServerErrorResponse,
    Pagination,
    GetMultipleDataResponse
)


router = APIRouter()


@router.get(
    path="",
    response_model=GetMultipleDataResponse[v2.BookEntity],
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {"model": NotFoundErrorResponse},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": InternalServerErrorResponse}
    }
)
async def get_books(
    country: Annotated[Country, Query(default=..., description="A country of book.")],
    language: Annotated[Language | None, Query(description="A language of book.")] = None,
    limit: Annotated[int, Query(ge=1, description="")] = 20,
    offset: Annotated[int, Query(ge=1, description="")] = 1
) -> GetMultipleDataResponse[v2.BookEntity]:
    """
    Description \n
        1. Get all books with specific country and language.

    To-do \n
        1. Search by name with query parameter.
    """
    return GetMultipleDataResponse(
        data=[
            v2.BookEntity(code="B0001", name="Demian", country="USA", language=Language.KOREAN),
            v2.BookEntity(code="B0002", name="Siddhartha", country="USA", language=Language.ENGLISH)            
        ],
        pagination=Pagination(page=1, limit=20, total=2)
    )
