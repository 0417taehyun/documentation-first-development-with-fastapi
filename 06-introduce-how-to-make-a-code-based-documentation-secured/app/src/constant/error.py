from enum import StrEnum


class ErrorType(StrEnum):
    UNAUTHORIZED: str = "unathorized"
    FORBIDDEN: str = "forbidden"
    NOT_FOUND: str = "not_found"
    INTERNAL_SERVER: str = "internal_server"
