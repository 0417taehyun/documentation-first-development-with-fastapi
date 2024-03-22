from typing import Annotated
from datetime import date

from pydantic import BaseModel, Field, EmailStr, computed_field


class AuthorBase(BaseModel):
    first_name: Annotated[
        str,
        Field(
            default=...,
            serialization_alias="firstName",
            description="The first name of the author.",
            examples=["Taehyun"]
        )
    ]
    last_name: Annotated[
        str,
        Field(
            default=...,
            serialization_alias="lastName",
            description="The last name of the author.",
            examples=["Lee"]
        )
    ]
    age: Annotated[
        int,
        Field(
            default=...,
            ge=19,
            description="The age of the author",
            examples=[19]
        )
    ]
    email: Annotated[
        EmailStr,
        Field(
            default=...,
            description="An email of the author.",
            examples=["0417taehyun@gmail.com"]
        )
    ]
    birth: Annotated[
        date,
        Field(
            default=...,
            description="A date of birth of the author.",
            examples=["1997-04-17"]
        )
    ]

    @computed_field(description="A full name of the author", examples=["Taehyun Lee"])
    @property
    def name(self) -> str:
        return " ".join([self.first_name, self.last_name])


class AuthorDTO(AuthorBase):
    first_name: Annotated[
        str,
        Field(
            default=...,
            validation_alias="firstName",
            serialization_alias="firstName",
            description="The first name of the author.",
            examples=["Taehyun"]
        )
    ]
    last_name: Annotated[
        str,
        Field(
            default=...,
            validation_alias="lastName",
            serialization_alias="lastName",
            description="The last name of the author.",
            examples=["Lee"]
        )
    ]
    

class AuthorEntity(AuthorBase):
    id: Annotated[
        str,
        Field(
            default=...,
            description="A unique id of the author.",
            examples=["A0001"]
        )
    ]
