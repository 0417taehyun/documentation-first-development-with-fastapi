from typing import Annotated

from pydantic import BaseModel, Field


class Book(BaseModel):
    name: Annotated[
        str,
        Field(
            default=...,
            description="Name of book.",
            examples=["Demian", "Siddhartha"]
        )
    ]
