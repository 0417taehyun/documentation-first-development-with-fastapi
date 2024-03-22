from fastapi import FastAPI

from src.constant import APIPath
from src.router.public import book, event


app = FastAPI(
    title="A public API",
    description="Describe how to seperate API through path for better security.",
    version="1.0.0",
    contact={"email": "0417taehyun@gmail.com"}       
)
app.include_router(router=book.router, prefix=APIPath.BOOKS.value, tags=["Book"])
app.include_router(router=event.router, prefix=APIPath.EVENTS.value, include_in_schema=False)
