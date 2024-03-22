from enum import StrEnum


class APIPath(StrEnum):
    BOOKS: str = "/books"
    AUTHORS: str = "/authors"
    

class APIVersion(StrEnum):
    V1: str = "/v1"
    V2: str = "/v2"
