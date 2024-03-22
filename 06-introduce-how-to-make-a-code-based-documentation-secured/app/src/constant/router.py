from enum import StrEnum


class APIPath(StrEnum):
    DOCUMENTATIONS: str = "/docs"
    BOOKS: str = "/books"
    EVENTS: str = "/events"
    AUTHORS: str = "/authors"


class APIBoundary(StrEnum):
    PRIVATE: str = "/private"
    PUBLIC: str = "/public"
    