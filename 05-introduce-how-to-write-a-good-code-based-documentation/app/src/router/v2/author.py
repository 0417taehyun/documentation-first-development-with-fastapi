from typing import Annotated

from fastapi import APIRouter, status, Path, Body

from src.schema import (
    v2,
    UnauthorizedErrorResponse,
    ForbiddenErrorResponse,
    NotFoundErrorResponse,
    InternalServerErrorResponse,
    GetDataResponse,
    CreateDataResponse
)


router = APIRouter()


@router.get(
    path="/{id}",
    response_model=GetDataResponse[v2.AuthorEntity],
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {"model": NotFoundErrorResponse},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": InternalServerErrorResponse}
    }
)
async def get_author(
    id: Annotated[str, Path(default=...,description="A unique id of the author.")]
) -> GetDataResponse[v2.AuthorEntity]:
    """
    Description \n
        1. Get a specific author by their unique id.
    """
    return GetDataResponse(data=v2.AuthorEntity(
        id=id, first_name="Taehyun", last_name="Lee", age=28, email="0417taehyun@gmail.com", birth="1997-04-17"
    ))


@router.post(
    path="",
    response_model=CreateDataResponse[v2.AuthorEntity],
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_401_UNAUTHORIZED: {"model": UnauthorizedErrorResponse},
        status.HTTP_403_FORBIDDEN: {"model": ForbiddenErrorResponse},
        status.HTTP_404_NOT_FOUND: {"model": NotFoundErrorResponse},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": InternalServerErrorResponse}
    }
)
async def create_authors(
    author: Annotated[v2.AuthorDTO, Body(default=..., description="An author object to create.")]
) -> CreateDataResponse[v2.AuthorEntity]:
    """
    Description \n
        1. Create an author.
        2. Return the entity of the author.
    """
    return CreateDataResponse(data=v2.AuthorEntity(
        id="A001", first_name="Taehyun", last_name="Lee", age=28,  email="0417taehyun@gmail.com", birth="1997-04-17"
    ))
