from typing import Annotated, Sequence

from pydantic import BaseModel, Field

from src.constant import ErrorType


class ErrorDetail(BaseModel):
    loc: Annotated[
        Sequence[str],
        Field(
            default=...,
            description="A location where the error occured.",
            examples=["authros", "A001"]
        )
    ]
    msg: Annotated[
        str,
        Field(
            default=...,
            description="A message of the error.",
            examples=["user is unauthorized", "entity is not found"]
        )
    ]
    type: Annotated[
        ErrorType,
        Field(
            default=...,
            description="A type of the error.",
            examples=[ErrorType.UNAUTHORIZED.value, ErrorType.NOT_FOUND.value]
        )
    ]


class ErrorResponse(BaseModel):
    detail: Annotated[ErrorDetail, Field(default=..., description="A detail of the error response.")]


class UnauthorizedErrorResponse(ErrorResponse):
    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "detail": {
                        "loc": ["authors", "token"],
                        "msg": "user is unauthorized.",
                        "type": ErrorType.UNAUTHORIZED.value,
                    }
                }
            ]
        }


class ForbiddenErrorResponse(ErrorResponse):
    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "detail": {
                        "loc": ["authors", "token"],
                        "msg": "user is forbidden.",
                        "type": ErrorType.FORBIDDEN.value,
                    }
                }
            ]
        }


class NotFoundErrorResponse(ErrorDetail):
    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "detail": {
                        "loc": ["books", "A002"],
                        "msg": "entity is not found.",
                        "type": ErrorType.NOT_FOUND.value,
                    }
                }
            ]
        }

class InternalServerErrorResponse(ErrorDetail):
    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "detail": {
                        "loc": ["can be everywhere :("],
                        "msg": "unhandled error",
                        "type": ErrorType.INTERNAL_SERVER.value,
                    }
                }
            ]
        }
