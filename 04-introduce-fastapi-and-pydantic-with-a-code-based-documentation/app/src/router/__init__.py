from fastapi import APIRouter

from src.router import book


router = APIRouter()

router.include_router(router=book.router, tags=["Book"])
