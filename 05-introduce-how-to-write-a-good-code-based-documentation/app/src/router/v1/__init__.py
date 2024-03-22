from fastapi import FastAPI

from src.constant import APIPath
from src.router.v1 import book


app = FastAPI(
    title="The first version of API",
    description="Describe the fundamental concept of DFD(Documentation-First Developmemt).",
    version="1.0.0",
    contact={"email": "0417taehyun@gmail.com"}    
)
app.include_router(router=book.router, prefix=APIPath.BOOKS.value, tags=["Book"])
