from typing import Annotated

from pydantic import BaseModel, Field

from src.constant import Country, Language


class BookEntity(BaseModel):
    name: Annotated[
        str,
        Field(
            default=...,
            description="A name of the book.",
            examples=["Demian", "Siddhartha"]
        )
    ]
    country: Annotated[
        Country,
        Field(
            default=...,
            description="A country of the book."
        )
    ]
    language: Annotated[
        Language,
        Field(
            default=...,
            description="A language of the book."
        )
    ]
