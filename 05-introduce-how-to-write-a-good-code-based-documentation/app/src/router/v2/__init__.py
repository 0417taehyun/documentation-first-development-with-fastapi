from fastapi import FastAPI

from src.constant import APIPath
from src.router.v2 import author, book


app = FastAPI(
    title="The second version of API",
    description="Describe how to write a good code-based documentation.",
    version="2.0.0",
    contact={"email": "0417taehyun@gmail.com"}
)
app.include_router(router=author.router, prefix=APIPath.AUTHORS.value, tags=["Author"])
app.include_router(router=book.router, prefix=APIPath.BOOKS.value, tags=["Book"])
