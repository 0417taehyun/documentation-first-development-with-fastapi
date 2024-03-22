from typing import TypeVar, Generic, Annotated, Sequence

from pydantic import BaseModel, Field


Data = TypeVar("Data", bound=BaseModel)


class Pagination(BaseModel):
    page: Annotated[
        int,
        Field(
            default=1,
            ge=1,
            description="A current page number.",
            examples=[1]
        )
    ]
    limit: Annotated[
        int, Field(
            default=20,
            ge=1,
            description="A number to limit the data.",
            examples=[20]
        )
    ]
    total: Annotated[
        int,
        Field(
            default=...,
            ge=1,
            description="A total number of the data.",
            examples=[100]
        )
    ]


class DataResponse(BaseModel, Generic[Data]):
    data: Annotated[Data, Field(default=..., description="A data object.")]


class CreateDataResponse(DataResponse, Generic[Data]):
    pass


class GetDataResponse(DataResponse, Generic[Data]):
    pass


class GetMultipleDataResponse(DataResponse, Generic[Data]):
    pagination: Annotated[
        Pagination,
        Field(
            default=...,
            description="A pagination object."
        )
    ]
    data: Annotated[
        Sequence[Data],
        Field(
            default=..., 
            description="A list of the data."
        )
    ]

