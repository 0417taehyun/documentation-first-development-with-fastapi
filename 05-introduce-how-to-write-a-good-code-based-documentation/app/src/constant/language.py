from enum import StrEnum
from typing import Literal


Country = Literal["USA", "KOREA"]


class Language(StrEnum):
    KOREAN: str = "korean"
    ENGLISH: str = "english"
